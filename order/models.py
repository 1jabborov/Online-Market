from django.db import models

# Create your models here.


class Order(models.Model):
    ORDER_STATUS = (
        ("created"),
        ("accepted"),
        ("completed"),
        ("canceled"),
    )

    client = models.ForeignKey("client.Client", verbose_name="Client", on_delete=models.PROTECT)
    warehouse = models.ForeignKey('warehouse.Warehouse', verbose_name="Base", on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(verbose_name="Created date", auto_now_add=True)
    status = models.CharField(verbose_name="Product status", max_length=255, choices=ORDER_STATUS)
    total = models.DecimalField(verbose_name="Price", max_digits=17, decimal_places=2, null=True)

    def __str__(self):
        return self.created_at.strftime("%d-%m-%Y")

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderItem(models.Model):
    order = models.ForeignKey("Order", verbose_name="Order", on_delete=models.PROTECT)
    warehouse_product = models.ForeignKey("warehouse.WarehouseProduct", verbose_name="Product", on_delete=models.PROTECT)
    price = models.DecimalField(verbose_name="Price", max_digits=17, decimal_places=2)
    count = models.IntegerField(verbose_name="Count")
    total = models.DecimalField(verbose_name="Amount", max_digits=17, decimal_places=2)

    def __str__(self):
        return self.warehouse_product.product.name

    class Meta:
        verbose_name = "Order unit"
        verbose_name_plural = "Order units"
