from django.db import models
from uuid import uuid4

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=264, verbose_name='Name')

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class Manufactory(models.Model):
    name = models.CharField(max_length=264, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    country = models.ForeignKey('Country', on_delete=models.PROTECT, verbose_name='Developed')

    class Meta:
        verbose_name = 'Manufacturing plant'
        verbose_name_plural = 'Manufacturing plants'

    def __str__(self):
        return self.name


class Category(models.Model):
    parent = models.ForeignKey('Category', verbose_name="Parent category", on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=264, verbose_name='Name')
    slug = models.SlugField(max_length=255)
    photo = models.FileField(verbose_name="Category photo", upload_to="product/category_images", null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name='Category')
    manufactory = models.ForeignKey('Manufactory', on_delete=models.PROTECT, related_name='manufactory_re', verbose_name='Manufactory', null=True)  # verbose_name
    country = models.ForeignKey('Country', on_delete=models.PROTECT, verbose_name='Country of origin', null=True, blank=True)
    sale_count = models.IntegerField(default=0, verbose_name='Count of sales')
    view_count = models.PositiveBigIntegerField(default=0, verbose_name='Number of views')
    is_active = models.BooleanField(default=True, verbose_name='Status active')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=264, verbose_name='Name')

    class Meta:
        verbose_name_plural = 'Feature'

    def __str__(self):
        return self.name


class ProductMedia(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='Product', related_name='product_media')
    media = models.FileField(upload_to='product/product_images', verbose_name='Video/Photo', null=True, blank=False)
    is_active = models.BooleanField(default=True, verbose_name='Status active')

    class Meta:
        verbose_name_plural = 'Product Videos/Photos'

    def __str__(self):
        return self.product.name


class ProductCharacter(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Product', related_name='product_character')
    character = models.ForeignKey('Character', on_delete=models.PROTECT, verbose_name='Product feature')
    value = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Product feature'

    def __str__(self):
        return self.product.name


class ProductPrice(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Product', related_name='product_price')
    unit_type = models.CharField(verbose_name="Unit of measure", max_length=255)
    price = models.DecimalField(max_digits=17, decimal_places=2, default=0, verbose_name='Price')
    is_active = models.BooleanField(default=True, verbose_name='Status active')

    class Meta:
        verbose_name_plural = 'Product price'

    def __str__(self):
        return self.product.name
    