from django.db import models

# Create your models here.


class OutlayCategory(models.Model):
    name = models.CharField(verbose_name="Outlay category", max_length=255)

    def __str__(self):
        return self.name


class Outlay(models.Model):
    name = models.CharField(verbose_name="Cost name", max_length=255)
    outlay_category = models.ForeignKey('OutlayCategory', verbose_name="Outlay category", on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class PaymentTransaction(models.Model):
    PAYMENT_MEYHOD = (
        ('cash'),
        ('card'),
        ('bank'),
    )
    PAYMENT_TYPE = (
        ('income'),
        ('order'),
        ('client'),
        ('provider'),
        ('outlay'),
    )
    TRANSACTION_TYPE = (
        ('income'),
        ('outcome')
    )
    payment_method = models.CharField(verbose_name="Payment method", max_length=255, choices=PAYMENT_MEYHOD)
    payment_type = models.CharField(verbose_name="Payment type", max_length=255, choices=PAYMENT_TYPE)
    transaction_type = models.CharField(verbose_name="Transaction type", max_length=50, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=17, decimal_places=2, verbose_name="Value")
    is_deleted = models.BooleanField(verbose_name="Deleted")
    comment = models.CharField(verbose_name="Comment", max_length=400)
    income = models.ForeignKey('income.Income', verbose_name="Product income", on_delete=models.PROTECT, null=True, blank=True)
    order = models.ForeignKey('order.Order', verbose_name="Order", on_delete=models.PROTECT, null=True, blank=True)
    client = models.ForeignKey('client.Client', verbose_name="Client", on_delete=models.PROTECT, null=True, blank=True)
    provider = models.ForeignKey('provider.Provider', verbose_name="Provider", on_delete=models.PROTECT, null=True, blank=True)
    outlay = models.ForeignKey('Outlay', verbose_name="Outlay name", on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    deleted_at = models.DateTimeField(auto_now_add=True, verbose_name="Deleted date", null=True, blank=True)
    created_user = models.ForeignKey('user.User', verbose_name="Created by the employee", on_delete=models.PROTECT, related_name='created_user')
    deleted_user = models.ForeignKey('user.User', verbose_name="Deleted employee", on_delete=models.PROTECT, null=True, blank=True, related_name='deleted_user')
