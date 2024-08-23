import ollama
from django.core.management.base import BaseCommand
from django.db import transaction
from properties_rewriter.models import Property, PropertySummary


class Command(BaseCommand):
    help = 'Rewrites property information and generates summaries using Ollama'

    def handle(self, *args, **options):
        properties = Property.objects.all()
        for property in properties:
            with transaction.atomic():
                new_title = self.rewrite_title(property.title)
                new_description = self.rewrite_description(property.description)

                property.title = new_title
                property.description = new_description
                property.save()

                self.stdout.write(self.style.SUCCESS(f'Rewritten Title: {new_title}'))
                self.stdout.write(self.style.SUCCESS(f'Rewritten Description: {new_description}'))

                summary = self.generate_summary(new_title, new_description, property)
                PropertySummary.objects.update_or_create(
                    property_info=property,
                    defaults={'summary': summary}
                )

                self.stdout.write(self.style.SUCCESS(f'Generated Summary: {summary}'))

            self.stdout.write(self.style.SUCCESS(f'Successfully processed property {property.property_id}'))

        self.stdout.write(self.style.SUCCESS('Successfully rewrote all properties and generated summaries'))

    def rewrite_title(self, title):
        title_prompt = f"Rewrite this title in a concise manner but relevant alternative name of : {title}. Give only option without any text response."
        title_response = ollama.generate(model='gemma2:2b', prompt=title_prompt)
        new_title = self.parse_response(title_response['response'], field='Title')
        return self.truncate_text(new_title, 200)

    def rewrite_description(self, description):
        description_prompt = f"Rewrite this description in a concise manner: {description}"
        description_response = ollama.generate(model='gemma2:2b', prompt=description_prompt)
        return self.parse_response(description_response['response'], field='Description')

    def generate_summary(self, title, description, property):
        locations = ", ".join([str(location) for location in property.locations.all()])
        amenities = ", ".join([str(amenity) for amenity in property.amenities.all()])
        summary_prompt = f"""Summarize the following property information:
        Title: {title}
        Description: {description}
        Locations: {locations}
        Amenities: {amenities}"""
        summary_response = ollama.generate(model='gemma2:2b', prompt=summary_prompt)
        return summary_response['response'].strip()

    def parse_response(self, response_text, field):
        response_text = response_text.strip()
        field = field.lower()

        if field == 'title':
            return self.extract_field(response_text, "Rewritten Title:")
        elif field == 'description':
            return self.extract_field(response_text, "Rewritten Description:")
        elif field == 'summary':
            return self.extract_field(response_text, "Generated Summary:")

        return response_text

    def extract_field(self, text, field_name):
        if field_name in text:
            start = text.find(field_name) + len(field_name)
            end = text.find("←", start)
            return text[start:end].strip() if end != -1 else text[start:].strip()
        return text

    def truncate_text(self, text, max_length):
        return text[:max_length] if len(text) > max_length else text