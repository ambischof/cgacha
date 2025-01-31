from django.urls import path
from . import views

app_name = "gacha"
urlpatterns = [
  path("", views.IndexView.as_view(), name="index" ),
  path("roll", views.RollView.as_view(), name="roll")
]