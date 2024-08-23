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
                # Rewrite title and description
                prompt = f"Rewrite the following property title and description:\nTitle: {property.title}\nDescription: {property.description}"
                response = ollama.generate(model='gemma2:2b', prompt=prompt)
                new_title, new_description = self.parse_rewrite(response['response'])
                
                property.title = new_title
                property.description = new_description
                property.save()

                # Print the rewritten title and description
                self.stdout.write(self.style.SUCCESS(f'Rewritten Title: {new_title}'))
                self.stdout.write(self.style.SUCCESS(f'Rewritten Description: {new_description}'))

                # Generate summary
                locations = ", ".join([str(location) for location in property.locations.all()])
                amenities = ", ".join([str(amenity) for amenity in property.amenities.all()])
                summary_prompt = f"""Summarize the following property information:
                Title: {property.title}
                Description: {property.description}
                Locations: {locations}
                Amenities: {amenities}"""
                summary_response = ollama.generate(model='gemma2:2b', prompt=summary_prompt)
                summary = summary_response['response'].strip()
                
                PropertySummary.objects.update_or_create(
                    property_info=property,
                    defaults={'summary': summary}
                )

                # Print the generated summary
                self.stdout.write(self.style.SUCCESS(f'Generated Summary: {summary}'))

            self.stdout.write(self.style.SUCCESS(f'Successfully processed property {property.property_id}'))

        self.stdout.write(self.style.SUCCESS('Successfully rewrote all properties and generated summaries'))

    def parse_rewrite(self, response):
        lines = response.strip().split('\n')
        new_title = lines[1].replace('Title: ', '')
        new_description = '\n'.join(lines[1:]).replace('Description: ', '')
        return new_title, new_description

