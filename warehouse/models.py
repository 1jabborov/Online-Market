from django.db import models
from product.models import Product

# Enter your models here.


class WarehouseProduct(models.Model):
    product = models.ForeignKey("product.Product", verbose_name="Product name", on_delete=models.PROTECT)
    count = models.IntegerField(verbose_name="Count")
    total = models.DecimalField(verbose_name="Total", max_digits=17, decimal_places=2, null=True)
    self_price = models.DecimalField(verbose_name="Self price", max_digits=17, decimal_places=2)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Warehouse product"
        verbose_name_plural = "Warehouse products"
