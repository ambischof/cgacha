from django.urls import path, include
from . import views

app_name = "gacha"
urlpatterns = [
  path("", views.IndexView.as_view(), name="index" ),
  path("roll", views.RollView.as_view(), name="roll"),
  path("testroll", views.TestRollView.as_view(), name="testroll"),
  path("itemlist", views.itemlist, name="itemlist"),
  path("allitems", views.AllItemList.as_view(), name="allitemslist"),
  path("addcredits", views.addcredits, name="addcredits"),

  path("accounts/register", views.register, name="register"),
  # many of these views are currently unimplemented
  #TODO: implement more views only views that are used
  path("accounts/", include("django.contrib.auth.urls"))
] 