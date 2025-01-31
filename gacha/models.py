from django.db import models
# from django.contrib.auth.models import User
from .lib import rarity
from django.db import transaction

# winnable items
class Item(models.Model):
  name = models.CharField(max_length=30, unique=True)
  
  # not sure how labels will work? documentation is scarce.
  class Rarities(models.IntegerChoices): 
    ONE = 1, '★',
    TWO = 2, '★★',
    THREE = 3, '★★★',
    FOUR = 4, '★★★★',
    FIVE = 5, '★★★★★'

  rarity = models.IntegerField(choices=Rarities, default=1)
  
  @staticmethod
  def get_random_item():
    rarityVal = rarity.get_random_rarity()
    return Item.objects.filter(rarity=rarityVal).order_by('?')[:1][0]
  
  def __str__(self):
    return self.name +' (' + str(self.rarity) + '★)'

# the user account
#TODO: make this into a proper authentication user model, 
#      but punting on that because I don't want to deal with 
#      logging in during development
class Account(models.Model):
  username = models.CharField(max_length=30, unique=True)
  # each user starts with 100 credits
  credits = models.IntegerField(default=100)
  items = models.ManyToManyField(Item, through="AccountItem")

  def __str__(self):
    return self.username



# relation between user and item
class AccountItem(models.Model):
  account = models.ForeignKey(Account, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  acquired = models.DateTimeField(auto_now_add=True)
  
  ''' the bread and butter of the app, trading credits for an item '''
  @staticmethod
  def roll(account: Account):
    if (account.credits < 1):
      raise Exception('Not enough Credits')

    item = Item.get_random_item()
    with transaction.atomic():
      account.credits -= 1
      account.save()
      association = AccountItem(account=account, item=item)
      association.save()


    return association

    