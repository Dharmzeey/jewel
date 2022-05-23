from django.db import models
from django.contrib.auth import settings

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  phone = models.CharField(max_length=11, unique=True)
  address = models.CharField(max_length=255)

  def __str__(self):
    return str(self.owner)
