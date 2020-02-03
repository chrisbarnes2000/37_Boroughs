# forms.py
from django import forms
from .models import *


class BoroughForm(forms.ModelForm):
    """ Render and process a form based on the Borough model. """
    class Meta:
        model = Borough
        fields = ['title', 'content', 'Main_Img']
