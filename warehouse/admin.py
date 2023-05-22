from django.contrib import admin
from .models import Warehouse, WarehouseProduct, Movement, MovementItem

# Register your models here.

admin.site.register([Warehouse, WarehouseProduct, Movement, MovementItem])
