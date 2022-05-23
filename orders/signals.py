# THIS IS WHEN THE ORDER HAS BEEN ACKNOWLEDGED AND THEN IT TRIGGERS THE COMPLETED_ORDER MODEL
from django.db.models.signals import post_save
from .models import Order, CompletedOrder


def create_completed_order(sender, instance, created, **kwargs):
  if created:
    if instance.status:
      CompletedOrder.objects.get_or_create(order_name=instance)


post_save.connect(create_completed_order, sender=Order)

