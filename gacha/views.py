from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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