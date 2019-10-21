from django.utils import timezone
from django.db import models
from django import forms
from .models import Product,Contact,Banertop
from django.contrib.admin import widgets  
from django.utils.translation import gettext_lazy as _


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','description','img', 'number','category']
        
class BannerTop(forms.ModelForm):
    class Meta:
        model = Banertop
        fields = ['banner_top']



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('Adinizi daxil edin...')}),
            'email': forms.TextInput(attrs={'placeholder': _('E-mail daxil edin...')}),
            'subject': forms.TextInput(attrs={'placeholder':_('Başlığ')}),
            'message': forms.Textarea(attrs={'placeholder': _('Probleminizi izah edin...' )})
        }
    