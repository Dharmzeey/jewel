from django.db import models


class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name


class Product(models.Model):
  name = models.CharField(max_length=60)
  price = models.IntegerField(default=0)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=1)
  description = models.CharField(max_length=250, default='', blank=True, null=True)
  image = models.ImageField(upload_to='uploads/products/%Y/%m/%d')

  def __str__(self):
    return self.name
