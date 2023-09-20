from django.db import models

# Create your models here.


class Customer_service(models.Model):
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_service_rep = models.CharField(max_length=100, blank=True, null=True)
    customer_phone = models.CharField(max_length=100, blank=True, null=True)
    customer_email = models.CharField(max_length=100, blank=True, null=True)
    customer_title = models.CharField(max_length=300, blank=True, null=True)
    customer_description = models.TextField(blank=True, null=True)
    ticket_date = models.DateTimeField(auto_now_add=True)
    ticket_status = models.BooleanField(default=False)
    order_number = models.IntegerField(blank=True, null=True)
    ticket_number = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'customer_service'
        verbose_name = 'Customer Service'
        verbose_name_plural = 'Customer Services'
        ordering = ['-ticket_date']
    def __str__(self):
        return self.customer_name
    
