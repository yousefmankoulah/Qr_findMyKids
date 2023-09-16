from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.


class GenerateQr(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(_('name'), max_length=300)
    type = models.CharField(_('type'), max_length=300, blank=True, null=True)
    address= models.CharField(_('address'), max_length=300, blank=True, null=True)
    phoneNumber= models.CharField(_('phoneNumber'), max_length=300)
    summary = models.TextField(_('summary'), blank=True, null=True)
    qr = models.ImageField(upload_to='media', blank=True)

    vistor_latitude = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    vistor_longitude = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)




    class Meta:
        ordering = ('name',)

    def __str__(self):
        return '{}'.format(self.parent)