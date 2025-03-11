from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Concat
from django.db import transaction
from .lib import rarity

# winnable items
class Item(models.Model):
  name = models.CharField(max_length=30, unique=True)
  flavor_text = models.CharField(max_length=200, blank=True)
  img_url = models.CharField(max_length=100, blank=True)
  
  # not sure how labels will work? documentation is scarce.
  class Rarities(models.IntegerChoices): 
    ONE = 1, '★',
    TWO = 2, '★★',
    THREE = 3, '★★★',
    FOUR = 4, '★★★★',
    FIVE = 5, '★★★★★'

  rarity = models.IntegerField(choices=Rarities, default=1)
  
  rarity_display = models.GeneratedField(
    expression= Concat(models.Value('('), 'rarity', models.Value('★)')),
    output_field=models.CharField(max_length=30),
    db_persist=False
  )
  
  @staticmethod
  def get_random_item():
    rarityVal = rarity.get_random_rarity()
    return Item.objects.filter(rarity=rarityVal).order_by('?')[:1][0]
  
  def __str__(self):
    return self.name +' ' + self.rarity_display

class Account(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  # each user starts with 100 credits
  credits = models.IntegerField(default=100)
  items = models.ManyToManyField(Item, through="AccountItem")
  
  def __str__(self):
    return self.user.username



# relation between user and item
class AccountItem(models.Model):
  account = models.ForeignKey(Account, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  acquired = models.DateTimeField(auto_now_add=True)
  
  ''' 
    the bread and butter of the app, trading credits for an item 
    this is a constructor
  '''
  @staticmethod
  def roll(account: Account):
    if (account.credits < 1):
      raise Exception('Not enough Credits')

    item = Item.get_random_item()
    account.credits -= 1
    association = AccountItem(account=account, item=item)

    # do a transaction here so that if roll fails, credit is 
    # not deducted
    with transaction.atomic():
      account.save()
      association.save()

    return association
  
  def __str__(self):
    return self.account.user.username + ' has ' + str(self.item)

    