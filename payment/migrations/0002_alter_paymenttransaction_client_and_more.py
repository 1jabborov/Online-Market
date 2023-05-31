# Generated by Django 4.2.1 on 2023-05-27 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenttransaction',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='paymenttransaction',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Cash'), ('card', 'Card'), ('bank', 'Bank')], max_length=255, verbose_name='Payment method'),
        ),
        migrations.AlterField(
            model_name='paymenttransaction',
            name='payment_type',
            field=models.CharField(choices=[('income', 'Income'), ('order', 'Order'), ('client', 'Client'), ('provider', 'Provider'), ('outlay', 'Outlay')], max_length=255, verbose_name='Payment type'),
        ),
        migrations.AlterField(
            model_name='paymenttransaction',
            name='transaction_type',
            field=models.CharField(choices=[('income', 'Income'), ('outcome', 'Outcome')], max_length=50, verbose_name='Transaction type'),
        ),
    ]