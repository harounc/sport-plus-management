from django.urls import path
from . import views
app_name = "actualites"
urlpatterns = [path("", views.list_news, name="list"), path("<slug:slug>/", views.detail, name="detail")]
