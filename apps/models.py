from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, DecimalField, DateTimeField, IntegerField, ForeignKey, CASCADE


class Category(Model):
    name = CharField(max_length=100)
    product_id = IntegerField(ForeignKey('apps.Product', CASCADE, related_name='categories'))


class Product(Model):
    name = CharField(max_length=100)
    price = DecimalField(decimal_places=2, max_digits=10)
    created = DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = DateTimeField(auto_now=True, null=True, blank=True)
