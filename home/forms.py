from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ProfileCreateForm(UserCreationForm):
  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")

    # THIS BELOW ENSURES THAT WE DO NOT HAVE DUPLICATE EMAIL
  def clean_email(self):
    email = self.cleaned_data['email']
    if User.objects.filter(email=email).exists():
      raise ValidationError("Email ALready Exists")
    return email


