from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.contrib.auth.models import User
from .models import AccountItem

class IndexView(LoginRequiredMixin, generic.DetailView):
  template_name = 'gacha/index.html'
  
  def get_object(self):
    model = self.request.user.account
    return model

class RollView(LoginRequiredMixin, generic.DetailView):
  model = AccountItem
  template_name = 'gacha/roll.html'
  def get_object(self):
    user = self.request.user.account
    accountItem = AccountItem.roll(user)
    return accountItem

#todo let user decide sortby
@login_required
def itemlist(request):
  account = request.user.account
  val = render(request, "gacha/itemlist.html", {
    "account": account, 
    "items": account.items.order_by('-rarity', 'name').all()
  })
  return val

class RegisterForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password', 'email', 'first_name', 'last_name']
    widgets ={
      "password": forms.PasswordInput(),
      "email": forms.EmailInput()
    }

def register(request):
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if (form.is_valid()):
      form.save()
      return redirect('gacha:login')
  else:
    form = RegisterForm()
    context = {
      "form": form, 
      "title": 'Register', 
      "action": "gacha:register"
    }
  return render (request, 'registration/form_wrapper.html', context)

