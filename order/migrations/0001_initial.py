# Generated by Django 4.2.1 on 2023-05-22 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('warehouse', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('status', models.CharField(choices=[('created', 'созданный'), ('accepted', 'потверждённый'), ('completed', 'завершённый'), ('canceled', 'отклонённый')], max_length=255, verbose_name='Product status')),
                ('total', models.DecimalField(decimal_places=2, max_digits=17, null=True, verbose_name='Price')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.client', verbose_name='Client')),
                ('warehouse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='warehouse.warehouse', verbose_name='Base')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Price')),
                ('count', models.IntegerField(verbose_name='Count')),
                ('total', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Amount')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.order', verbose_name='Order')),
                ('warehouse_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='warehouse.warehouseproduct', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Order unit',
                'verbose_name_plural': 'Order units',
            },
        ),
    ]
