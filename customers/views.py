from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect

from .models import Profile
from .forms import ProfileUpdateForm


# Create your views here.
class ProfileUpdateView(LoginRequiredMixin, View):
  template_name = 'registration/register.html'
  model = Profile
  success_url = 'profile:update'

  def get(self, request):
    owner = get_object_or_404(self.model, user=request.user)
    form = ProfileUpdateForm(instance=owner)
    context = {'form': form}
    return render(request, self.template_name, context)

  def post(self, request):
    owner = get_object_or_404(self.model, user=request.user)
    form = ProfileUpdateForm(request.POST, request.FILES, instance=owner)
    if not form.is_valid():
      context = {'form': form}
      return render(request, self.template_name, context)
    form.save()
    return redirect(self.success_url)
