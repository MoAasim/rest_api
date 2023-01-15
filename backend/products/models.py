from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=99.99)

    def __str__(self):
        return self.name