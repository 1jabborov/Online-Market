from django.contrib import admin
from .models import Income, IncomeItem

# Register your models here.

admin.site.register([Income, IncomeItem])
