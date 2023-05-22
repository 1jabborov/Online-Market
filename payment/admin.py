from django.contrib import admin
from .models import OutlayCategory, Outlay, PaymentTransaction

# Register your models here.

admin.site.register([OutlayCategory, Outlay, PaymentTransaction])
