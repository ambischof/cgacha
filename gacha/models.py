from django.db import models
from .lib import rarity

# winnable items
class Item(models.Model):
  name = models.CharField(max_length=30)
  
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
class Account(models.Model):
  username = models.CharField(max_length=30, primary_key=True)
  # each user starts with 100 credits
  credits = models.IntegerField(default=100)
  items = models.ManyToManyField(Item, through="AccountItem", through_fields=("username", "item"))



# relation between user and item
class AccountItem(models.Model):
  username = models.ForeignKey(Account, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  acquired = models.DateTimeField(auto_now_add=True)
  
  ''' the bread and butter of the app, trading credits for an item '''
  @staticmethod
  def roll(account):
    if (account.credits < 1):
      raise Exception('Not enough Credits')

    account.credits -= 1
    account.save()
    item = Item.get_random_item()
    try:
      association = AccountItem(username=account, item=item)
      association.save()
    
    #TODO: figure out transactions to make sure credits only are
    # taken when roll is successful
    except Exception as e:
      account.credits += 1
      account.save()
      raise e

    return item

    