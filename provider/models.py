from django.db import models

# Create your models here.


class Provider(models.Model):
    name = models.CharField(verbose_name="Provider", max_length=255)
    phone = models.CharField(max_length=13)
    balance = models.DecimalField(verbose_name="Balance", max_digits=17, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"
