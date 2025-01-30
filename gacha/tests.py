from django.test import TestCase
from .lib import rarity
from .models import Item, Account, AccountItem
import re

def make_items():
  items = []
  for x in range(1,6): 
      for y in range(1,4):
        items.append(Item.objects.create(name="item "+str(x)+str(y), rarity=x))
  return items


class RarityTests(TestCase): 
  def tests_are_spreading_correctly(self):
    accumulator = {
      "1": 0,
      "2": 0,
      "3": 0,
      "4": 0,
      "5": 0
    }

    TIMES = 10000
    """ 
      We're going to get 100,000 random numbers, and make sure their percents
      align with what we'd expect.
    """

    for x in range(TIMES):
      num = str(rarity.get_random_rarity())
      accumulator[num] += 1

    for x in range(1,6): 
      percent = accumulator[str(x)] / TIMES;
      self.assertAlmostEqual(percent, rarity.item_rarities_percent[str(x)], delta=.01)


class ItemTests(TestCase):
  # for each 5 rarities, create 3 items
  @classmethod
  def setUpTestData(cls):
    cls.items = make_items()
    

  def test_can_get_random_item(self):
    rando = Item.get_random_item()
    reg = re.compile('^item \d\d')
    self.assertTrue(reg.match(rando.name))
    

class AccountItemTests(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.user = Account(username="Sally")
    cls.broke_user = Account(username="brokeJoe", credits=0)
    cls.items = make_items()
  
  def test_roll(self):
    item = AccountItem.roll(self.user)
    self.assertEqual(self.user.credits, 99)
    self.assertEqual(item, self.user.items.all()[0])

  def test_credit_check(self):
    with self.assertRaisesMessage(Exception, 'Not enough Credits'):
      item = AccountItem.roll(self.broke_user)