from django import forms
from .models import CommentPost

from django.utils.translation import gettext_lazy as _


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = CommentPost
        fields = ('user','comment',)
        widgets = {
            'user':  forms.TextInput(attrs={'placeholder': _('Adınızı daxil edin...')}),
            'comment':  forms.Textarea(attrs={'placeholder': 'Fikirinizi təsvir edin...'}),
        }
    

