from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import ProfileCreateForm


class Home(View):
  template_name = 'home/home.html'

  def get(self, request):

    return render(request, self.template_name)


class Signup(CreateView):
  form_class = ProfileCreateForm
  template_name = 'registration/register.html'
  success_url = reverse_lazy("login")
