# script for adding the items back when I'd like to nuke the db

from gacha import models
import json

with open('items.json', 'r') as file:
    items = json.load(file)


def addItems():
  user = models.Account(username="defaultUser")
  user.save()

  for i in items: 
    newItem = models.Item(name= i["name"], rarity=i["rarity"])
    newItem.save()