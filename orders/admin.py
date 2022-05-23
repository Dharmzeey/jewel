from django.contrib import admin
from .models import Order, CompletedOrder


admin.site.register(Order)
admin.site.register(CompletedOrder)