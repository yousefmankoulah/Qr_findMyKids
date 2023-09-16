from django.db import models
from home.models import GenerateQr
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Order(models.Model):
    token = models.CharField(max_length=250, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='USD Order Total')
    emailAddress = models.EmailField(max_length=250, blank=True, verbose_name='Email Address')
    created = models.DateTimeField(auto_now_add=True)
    billingName = models.CharField(_('billingName'), max_length=250, blank=True)
    billingAddress1 = models.CharField(_('billingAddress1'), max_length=250, blank=True)
    billingCity = models.CharField(_('billingCity'), max_length=250, blank=True)
    billingPostcode = models.CharField(_('billingPostcode'), max_length=10, blank=True)
    billingCountry = models.CharField(_('billingCountry'), max_length=200, blank=True)
    shippingName = models.CharField(_('shippingName'), max_length=250, blank=True)
    shippingAddress1 = models.CharField(_('shippingAddress1'), max_length=250, blank=True)
    shippingCity = models.CharField(_('shippingCity'), max_length=250, blank=True)
    shippingPostcode = models.CharField(_('shippingPostcode'), max_length=10, blank=True)
    shippingCountry = models.CharField(_('shippingCountry'), max_length=200, blank=True)
    ready_to_ship = models.BooleanField(default=False, blank=True, null=True)
    ship = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'Order'
        ordering = ['-created']
    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.CharField(_('product'), max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    parent = models.ForeignKey(GenerateQr, on_delete=models.CASCADE, default="")
    kids_name = models.CharField(_('kids_name'), max_length=250, blank=True, null=True)
    qr = models.ImageField(upload_to='media', blank=True, null=True)

   

    class Meta:
        db_table = 'OrderItem'
    def sub_total(self):
        return self.quantity * self.price
    def __str__(self):
        return self.product