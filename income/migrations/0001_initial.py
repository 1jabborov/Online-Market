# Generated by Django 4.2.1 on 2023-05-27 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('provider', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('status', models.CharField(choices=[('created', 'Created'), ('accepted', 'Accepted'), ('completed', 'Complated'), ('canceled', 'Canceled')], default='created', max_length=255, verbose_name='Status')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Price')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='provider.provider', verbose_name='Provider')),
            ],
            options={
                'verbose_name': 'Product input',
                'verbose_name_plural': 'Product inputs',
            },
        ),
        migrations.CreateModel(
            name='IncomeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Price')),
                ('count', models.IntegerField(verbose_name='Count')),
                ('total', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Amount')),
                ('income', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='income.income', verbose_name='Income input')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product input',
                'verbose_name_plural': 'Product inputs',
            },
        ),
    ]
