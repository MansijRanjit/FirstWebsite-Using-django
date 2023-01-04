from django.urls import path
from .views import *

app_name ="everestapp"

urlpatterns = [
  path("",ClientHomeView.as_view(), name="clienthome"),
  path("service/",ClientServiceView.as_view(), name="clientservice"),
  path("about/",ClientAboutView.as_view(), name="clientabout"),
  path("contact/",ClientContactView.as_view(), name="clientcontact"),
  path("news/",ClientNewsView.as_view(), name="clientnews"),


]
