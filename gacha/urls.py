from django.urls import path, include
from . import views

app_name = "gacha"
urlpatterns = [
  path("", views.IndexView.as_view(), name="index" ),
  path("roll", views.RollView.as_view(), name="roll"),
  path("itemlist", views.itemlist, name="itemlist"),
  # many of these views are currently unimplemented
  #TODO: implement more views only views that are used
  path("accounts/", include("django.contrib.auth.urls"))
]