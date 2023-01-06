from django.shortcuts import render

# Create your views here.

from django.views.generic import View, TemplateView,ListView,DetailView, CreateView,UpdateView,DeleteView
from .models import *
from .forms import*
from django.urls import reverse, reverse_lazy

class ClientHomeView(TemplateView):
  template_name ="clienthome.html"

class ClientServiceView(TemplateView):
  template_name ="clientservice.html"

class ClientAboutView(ListView):
  template_name ="clientabout.html"
  model = Category
  context_object_name ='categories'

class ClientContactView(TemplateView):
  template_name ="clientcontact.html"

class ClientNewsView(ListView):
  template_name ="clientnews.html"
  model = News
  context_object_name='news'

class ClientNewsDetailView(DetailView):
  template_name="clientnewsdetail.html"
  model= News
  context_object_name ="newsdetails"

class ClientNewsCreateView(CreateView):
  template_name ="clientnewscreate.html"
  form_class = ClientNewsCreateForm
  model = News
  success_url = reverse_lazy("everestapp:clienthome")

class ClientNewsUpdateView(UpdateView):
  template_name ="clientnewscreate.html"
  form_class = ClientNewsCreateForm
  model = News
  success_url = reverse_lazy("everestapp:clienthome")

class ClientNewsDeleteView(DeleteView):
  template_name ="clientnewsdelete.html"
  model = News
  context_object_name= "news"
  success_url = reverse_lazy("everestapp:clienthome")