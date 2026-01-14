from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.db.models import Count
from django.contrib.auth.models import User
from .models import AccountItem, Item, Account

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
  
# to view the roll page without changing state
# Disable in production
class TestRollView(LoginRequiredMixin, generic.DetailView):
  model = AccountItem
  template_name = 'gacha/roll.html'
  def get_object(self):
    user = self.request.user.account
    item = user.items.first()
    return AccountItem(account=user, item=item)

#todo let user decide sortby
@login_required
def itemlist(request):
  account = request.user.account
  items = account.items.values().annotate(total=Count('pk')).order_by('total');
  val = render(request, "gacha/itemlist.html", {
    "account": account, 
    "items": items.order_by('-rarity', 'name').all()
  })
  return val

# Action only, do action and redirect
@login_required
def addcredits(request):
  account = request.user.account
  account.credits += 100
  account.save()
  return redirect("gacha:index")

class AllItemList(generic.ListView):
  class Meta:
    model = Item
  queryset = Item.objects.order_by('rarity')
  template_name = "gacha/all_item_list.html"

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
      # create the user but don't save it to the database
      # because it won't save the password right.
      user = form.save(commit=False)
      user.set_password(form.data['password'])
      user.save()
      # create the associated account too
      Account.objects.create(user=user)
      return redirect('gacha:login')
    else:
      context = {
        "form": form, 
        "title": 'Register', 
        "action": "gacha:register"
    }
  else:
    form = RegisterForm()
    context = {
      "form": form, 
      "title": 'Register', 
      "action": "gacha:register"
    }
  return render (request, 'registration/form_wrapper.html', context)

