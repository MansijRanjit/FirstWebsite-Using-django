from django.shortcuts import render

# Create your views here.

from django.views.generic import View, TemplateView

class ClientHomeView(TemplateView):
  template_name ="clienthome.html"

class ClientServiceView(TemplateView):
  template_name ="clientservice.html"

class ClientAboutView(TemplateView):
  template_name ="clientabout.html"

class ClientContactView(TemplateView):
  template_name ="clientcontact.html"

class ClientNewsView(TemplateView):
  template_name ="clientnews.html"