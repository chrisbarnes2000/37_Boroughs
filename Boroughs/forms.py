# forms.py
from django import forms
from .models import *


class BoroughForm(forms.ModelForm):
    class Meta:
        model = Borough
        fields = ['name', 'borough_Main_Img']
