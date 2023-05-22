from django.db import models
from product.models import Product

# Create your models here.


class Warehouse(models.Model):
    name = models.CharField(verbose_name="Base name", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Base"
        verbose_name_plural = "Bases"


class WarehouseProduct(models.Model):
    warehouse = models.ForeignKey("Warehouse", verbose_name="Base", on_delete=models.PROTECT)
    product = models.ForeignKey("product.Product", verbose_name="Product name", on_delete=models.PROTECT)
    count = models.IntegerField(verbose_name="Count")
    total = models.DecimalField(verbose_name="Amount", max_digits=17, decimal_places=2, null=True)
    self_price = models.DecimalField(verbose_name="The actual price of the product", max_digits=17, decimal_places=2)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Base product"
        verbose_name_plural = "Base products"


class Movement(models.Model):
    MOVEMENT_STATUS = (
        ("created", "созданный"),
        ("accepted", "потверждённый"),
        ("completed", "завершённый"),
        ("canceled", "отклонённый"),
    )
    from_warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT, related_name="from_warehouse", verbose_name="From warehouse")
    to_warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT, related_name="to_warehouse", verbose_name="To warehouse")
    status = models.CharField(verbose_name="Status", max_length=255, choices=MOVEMENT_STATUS, null=True)


class MovementItem(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.PROTECT, verbose_name="Excerpt")
    warehouse_product = models.ForeignKey(WarehouseProduct, on_delete=models.PROTECT, verbose_name="Product")
    count = models.IntegerField(verbose_name="Product count")
