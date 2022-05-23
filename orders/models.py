from django.db import models

from datetime import datetime
import random

from products.models import Product
from customers.models import Profile


class Favourites(models.Model):
  owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner_favourites')
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_favourites')


class Order(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner_orders')
  quantity = models.IntegerField(default=1)
  price = models.IntegerField()
  address = models.CharField(max_length=50, default='', blank=True)
  phone = models.CharField(max_length=50, default='', blank=True)
  date = models.DateTimeField(auto_now_add=True)
  status = models.BooleanField(default=False)

  def __str__(self):
    return '%s for %s' % (self.product, self.owner)
    # return f'{str(self.product)} for {str(self.owner)}'


class CompletedOrder(models.Model):
  order_name = models.ForeignKey(Order, on_delete=models.CASCADE)
  tracking_digit = random.randint(100000000000000, 999999999999999)
  tracking_number = models.CharField(max_length=20, default=tracking_digit)
  delivered = models.BooleanField(default=False)
  date_delivered = models.DateTimeField(auto_now=True)

  def __str__(self):
    return 'Tracking %s order %s' % (self.tracking_number, self.order_name)

  def get_tracking_number(self):
    while Order.objects.filter(tracking_number=self.tracking_number).exists():
      self.tracking_number = random.randint(100000000000000, 999999999999999)
    self.save()

