from django.db import models
from home.models import GenerateQr
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Category(models.Model):
    name = models.CharField(_('name'), max_length=250, unique=True)
    slug = models.SlugField(_('slug'), max_length=250, unique=True)
    description = models.TextField(_('description'), blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return '{}'.format(self.name)



class Product(models.Model):
    name = models.CharField(_('name'), max_length=250, unique=True)
    slug = models.SlugField( max_length=250, unique=True)
    description = models.TextField(_('description'), blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product')
    image2 = models.ImageField(upload_to='product', blank=True, null=True)
    image3 = models.ImageField(upload_to='product', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return '{}'.format(self.name)


