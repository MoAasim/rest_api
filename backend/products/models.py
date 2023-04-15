from django.db import models
from django.conf import settings
from django.db.models import Q

# Create your models here

User = settings.AUTH_USER_MODEL # auth.User.

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup = Q(name__icontains=query) | Q(description__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user)


class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True ,on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True, auto_created=True)
    createt_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)


    objects = ProductManager()

    def __str__(self):
        return self.name