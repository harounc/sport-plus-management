from django.urls import path
from . import views
app_name = "pages"
urlpatterns = [path("", views.home, name="home"), path("a-propos/", views.about, name="about"), path("services/", views.services, name="services"), path("contact/", views.contact, name="contact"), path("mentions-legales/", views.legal, name="legal"), path("confidentialite/", views.privacy, name="privacy")]
