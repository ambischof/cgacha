from django.views import generic
from .models import Account, AccountItem

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


