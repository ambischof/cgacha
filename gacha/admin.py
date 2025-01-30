from django.contrib import admin
from .models import Item, Account

class ItemAdmin(admin.ModelAdmin):
  ordering = ['rarity']
admin.site.register(Item, ItemAdmin)

admin.site.register(Account)
