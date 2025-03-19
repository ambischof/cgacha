# Crappy Gacha

implement a crappy gacha game

**Gacha Game** a user has a certain number of credits, and can exchange credit to get a random item from a list. Different items will have different probabilities and better items will usually have lower probabilities.

This document is the planning for _before_ implementing and is likely to be innacurate, see README for up to date info

## Purpose

 - Practice making a server in python, specifically django
 - ~~Brush up on AWS Deployment~~ NOPE this is NOT cost effective on a personal level. Finding alternative hosting
 - ~~Tailwind practice~~ On second thought, Tailwind is overkill for this project. Using Bootstrap.

## Project Overview
### MVP Version
Various features can be punted on during development cycle
- ~~No server just a program controller (is too minimum?)~~
- no account, just singular user
- ~~no database, just in program memory~~
- ~~no credits, unlimited rolls~~
- ~~command line based UI~~

### Components

- Winnable Items
- Database
- Server
- UI

### Controller functionality

#### Server Commands

- ☑ Roll 
- ☑ List owned 
- ☐ List possible (done but not exposed)
- ☐ View item details
- ☑ See credit 
- ☐ Buy credits (not with real money lolol)
- ☑ Create account
- ☑ Log in/Log out
- ☐ password change etc

### Database Shtuff

- Account
  - Id
  - Name
  - \# of credits
- Item
  - Id
  - Name
  - Rarity
- AccountItem
  - AccountId
  - ItemId
  - TimeAcquired

### Winnable Items

Percentages: 

| rarity | percent |
|---|---|
| 1* | 40% |
| 2* | 30% |
| 3* | 20% |
| 4* | 9% |
| 5* | 1% |
| total | 100% |


Eventually could include items and images. That would be less of a "crappy" gacha though.

(EDIT: it's me, of __course__ images were made lol)

### UI
Possibilities: 

- command line *(nope)*
- html (browser) *(yes)*
- discord *(unlikely)*


## todo 
Since i'm currently not using a more formal tracking system. (`!!!` indicates priority)

- ☐ Add about page !!!
- ☐ make more mobile friendly !!!
- ☐ add crispy for bootstrap form themes !
- ☐ make sure all images are square (and same size)? so image sizes can be specified in html !!!