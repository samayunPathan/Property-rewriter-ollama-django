from django.db import models


class Location(models.Model):
    LOCATION_TYPES = [
        ('country', 'Country'),
        ('state', 'State'),
        ('city', 'City'),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=LOCATION_TYPES)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['name', 'type']
        verbose_name_plural = "Locations"
        managed = False
        db_table = 'properties_location'

    def __str__(self):
        return f"{self.get_type_display()}: {self.name}"


class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Amenities"
        managed = False
        db_table = 'properties_amenity'

    def __str__(self):
        return self.name


class Property(models.Model):
    property_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    locations = models.ManyToManyField('Location')
    amenities = models.ManyToManyField('Amenity')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Properties"
        managed = False
        db_table = 'properties_property'

    def __str__(self):
        return self.title


class PropertySummary(models.Model):
    property_info = models.ForeignKey(Property, on_delete=models.CASCADE)
    summary = models.TextField()

    class Meta:
        db_table = 'property_summary'
        verbose_name_plural = "Property Summaries"

    def __str__(self):
        return f"Summary for {self.property_info.title}"