from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class GenerateQr(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=300, blank=True, null=True)
    address= models.CharField(max_length=300, blank=True, null=True)
    phoneNumber= models.CharField(max_length=300)
    summary = models.TextField(blank=True, null=True)
    qr = models.ImageField(upload_to='media', blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return '{}'.format(self.parent)