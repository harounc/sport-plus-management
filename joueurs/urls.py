from django.urls import path
from . import views
app_name = "joueurs"
urlpatterns = [path("", views.list_players, name="list"), path("<slug:slug>/", views.detail, name="detail")]
