from django.shortcuts import render
from django.views import generic
from .models import Account, AccountItem, Item
from django.http import Http404

class IndexView(generic.DetailView):
  template_name = 'gacha/index.html'
  
  def get_object(self):
    model = Account.objects.first()
    return model

class RollView(generic.DetailView):
  model = AccountItem
  template_name = 'gacha/roll.html'
  def get_object(self):
    user = Account.objects.first()
    accountItem = AccountItem.roll(user)
    return accountItem

#todo let user decide sortby
def itemlist(request):
  try:
    account = Account.objects.first();
  except Account.DoesNotExist:
    raise Http404("account does not exist")
  val = render(request, "gacha/itemlist.html", {
    "account": account, 
    "items": account.items.order_by('-rarity', 'name').all()
  })
  return val