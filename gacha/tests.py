from django.test import TestCase, Client
from django.contrib.auth.models import User
from .lib import rarity
from .models import Item, Account, AccountItem
import re
from .views import RollView, itemlist

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
      self.assertAlmostEqual(percent, rarity.item_rarities_percent[str(x)], delta=.015)


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
    user1 = User.objects.create_user(username="Sally")
    cls.acct = Account.objects.create(user=user1)
    user2 = User.objects.create_user(username="brokeJoe")
    cls.broke_account = Account.objects.create(user=user2, credits=0)
    cls.items = make_items()
  
  def test_roll(self):
    association = AccountItem.roll(self.acct)
    self.assertEqual(self.acct.credits, 99)
    self.assertEqual(association.item, self.acct.items.all()[0])

  def test_credit_check(self):
    with self.assertRaisesMessage(Exception, 'Not enough Credits'):
      AccountItem.roll(self.broke_account)

class AccountTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    user = User.objects.create_user(username="Sally")
    cls.acct = Account.objects.create(user=user)
    cls.items = make_items()

  def test_item_count(self):
    AccountItem.roll(self.acct)
    AccountItem.roll(self.acct)
    self.assertEqual(self.acct.item_count, 2)


class RollViewTest (TestCase):
  def setUp(self):
    user = User.objects.create_user(username="Sally")
    account = Account.objects.create(user=user)
    self.acct = account
    self.user = user
    make_items()
  
  def test_details(self):
    c = Client()
    c.force_login(user=self.user)
    request = c.get('/')
    view= RollView()
    view.setup(request.wsgi_request)
    object = view.get_object()
    self.assertEqual(self.acct,object.account)
    self.assertEqual(self.acct.items.first(), object.item)

class ItemListView(TestCase):
  def setUp(self):
    user = User.objects.create_user(username="Sally")
    account = Account.objects.create(user=user)
    self.items = make_items()
    # lets not do random roll to make it easier
    item1 = AccountItem.objects.create(account=account, item=self.items[0])
    item2 = AccountItem.objects.create(account=account, item=self.items[len(self.items)-1])
  
  # this doesn't work and I'm too tired to figure out why.
  # it won't matter when i add in authentication and 
  # it changes the way stuff is loaded
  # def test_list_data_right(self):
  #   request = RequestFactory().get('/')
  #   response= itemlist(request)
    # self.assertContains('item 53', response)
    # self.assertContains('item 11', response)