import random

# cumulative percentages
item_rarities_cum = {
  "1": 1,
  "2": .6,
  "3": .3,
  "4": .10,
  "5": .01
}
item_rarities_percent = {
  "1": .4,
  "2": .3,
  "3": .2,
  "4": .09,
  "5": .01
}

def get_random_rarity():
  # get a random number, then see which it aligns with on the cumulative map
  num = random.random()

  for x in range(5,0, -1): 
    if num <= item_rarities_cum[str(x)]:
      return x