

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    PROPERTY_TYPES = [
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
    ]
    agent = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)    
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPES)
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    image = models.ImageField(upload_to='properties/', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title