from django import forms
from .models import *


class jounralForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['journalName', 'journalFile']
