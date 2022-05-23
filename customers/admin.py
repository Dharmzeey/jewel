from django.contrib import admin
from .models import Profile


class CustomerAdmin(admin.ModelAdmin):
  list_display = ('owner', 'first_name', 'last_name', 'phone')


admin.site.register(Profile, CustomerAdmin)
