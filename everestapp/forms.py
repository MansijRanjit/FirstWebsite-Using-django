from django import forms
from .models import *

class ClientNewsCreateForm(forms.ModelForm):
  class Meta:
    model = News
    fields = "__all__"
    widgets ={
      'title': forms.TextInput(attrs={
        'class':'form-control',
      }),
      'category': forms.Select(),
      # 'content': SummernoteWidget(attrs={
      #   'summernote':{
      #     'class':'form-control form-control-rounded',
      #     'placeholder' : 'Page Description',
      #   }
      # }),
      'image' : forms.ClearableFileInput(),
    }