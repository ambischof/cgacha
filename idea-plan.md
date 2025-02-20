# Crappy Gacha

implement a crappy gacha game

**Gacha Game** a user has a certain number of credits, and can exchange credit to get a random item from a list. Different items will have different probabilities and better items will usually have lower probabilities.

This document is the planning for _before_ implementing and is likely to be innacurate, see README for up to date info

## Purpose

Practice making a server in python, specifically django
Brush up on AWS Deployment
Tailwind practice

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
- ☐ List possible
- ☐ View item details
- ☐ Create account
- ☑ See credit 
- ☐ Buy credits (not with real money lolol)
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

### UI
Possibilities: 

- command line
- html (browser)
- discord