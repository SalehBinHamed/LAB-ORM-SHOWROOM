from django.db import models
from brands.models import Brand
# Create your models here.
class Color(models.Model):
    color = models.CharField(max_length=128 , unique=True)

    def __str__(self) -> str:
        return self.color





class Cars(models.Model):

    YEAR_CHOICES = [(year, str(year)) for year in range(1952, 2024)]
    name = models.CharField(max_length=128 , unique=True) 
    year = models.IntegerField(choices=YEAR_CHOICES)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=False, default=1)  
    colors = models.ManyToManyField(Color)
    photo = models.ImageField(upload_to='car_photos/', null=True, blank=True)
    specs = models.TextField(null=True, blank=True)
    






