from django.db import models

# Create your models here.


class Income(models.Model):
    INCOME_STATUS = (
        ("created", "Created"),
        ("accepted", "Accepted"),
        ("completed", "Complated"),
        ("canceled", "Canceled")
    )
    provider = models.ForeignKey('provider.Provider', verbose_name="Provider", on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name="Created date", auto_now_add=True)
    status = models.CharField(verbose_name="Status", max_length=255, choices=INCOME_STATUS, default="created")
    total = models.DecimalField(verbose_name="Price", max_digits=17, decimal_places=2, default=0)

    def __str__(self):
        return self.created_at.strftime("%d-%m-%Y")

    class Meta:
        verbose_name = "Product input"
        verbose_name_plural = "Product inputs"


class IncomeItem(models.Model):
    income = models.ForeignKey("Income", verbose_name="Income input", on_delete=models.PROTECT)
    product = models.ForeignKey("product.Product", verbose_name="Product", on_delete=models.PROTECT)
    price = models.DecimalField(verbose_name="Price", max_digits=17, decimal_places=2)
    count = models.IntegerField(verbose_name="Count")
    total = models.DecimalField(verbose_name="Amount", max_digits=17, decimal_places=2)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Product input"
        verbose_name_plural = "Product inputs"
