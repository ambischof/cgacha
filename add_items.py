# script for adding the items back when I'd like to nuke the db

from gacha import models
import json
from django.contrib.auth.models import User

with open('items.json', 'r') as file:
    items = json.load(file)


def addItems():
  # assumes you named your user defaultuser
  user = User.objects.get(username='defaultuser')
  models.Account.objects.create(user=user)

  for i in items: 
    models.Item.objects.create(
       name= i["name"], 
       rarity=i["rarity"],
       flavor_text = i['flavor'],
       img_url = i['img']
    )
addItems()