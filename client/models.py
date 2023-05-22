from django.db import models

# Create your models here.


class Client(models.Model):
    full_name = models.CharField(verbose_name="Enter the full name of client.", max_length=255)
    phone = models.CharField(verbose_name="Enter the phone number of client.", max_length=13)
    balance = models.DecimalField(verbose_name="Balance", max_digits=17, decimal_places=2)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
