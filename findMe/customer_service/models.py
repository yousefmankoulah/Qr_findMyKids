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
    ticket_status = models.BooleanField(default=False, blank=True, null=True)
    order_number = models.CharField(max_length=300,blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.customer_name = self.customer_name.lower()
        self.customer_service_rep = self.customer_service_rep.lower()
        self.customer_email = self.customer_email.lower()
        self.customer_title = self.customer_title.lower()
        self.customer_description = self.customer_description.lower()
        self.category = self.category.lower()
        return super(Customer_service, self).save(*args, **kwargs)

    class Meta:
        db_table = 'customer_service'
        verbose_name = 'Customer Service'
        verbose_name_plural = 'Customer Services'
        ordering = ['-ticket_date']
    def __str__(self):
        return self.customer_name
    
