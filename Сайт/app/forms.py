"""
Definition of forms.
"""

from django import forms
from django.utils.translation import gettext_lazy as _

class ExamScoresForm(forms.Form):  
    russian = forms.IntegerField(min_value=0, max_value = 100, label='Russian', required= False)
    physics = forms.IntegerField(min_value=0, max_value = 100,label='Physics', required= False)
    literature = forms.IntegerField(min_value=0, max_value = 100,label='Literature', required= False)
    history = forms.IntegerField(min_value=0, max_value = 100,label='History', required= False)
    math = forms.IntegerField(min_value=0, max_value = 100,label='Math', required= False)
    chemistry = forms.IntegerField(min_value=0, max_value = 100,label='Chemistry', required= False)
    geography = forms.IntegerField(min_value=0, max_value = 100,label='Geography', required= False)
    socialstudies = forms.IntegerField(min_value=0, max_value = 100,label='Socialstudies', required= False)
    informatics = forms.IntegerField(min_value=0, max_value = 100,label='Informatics', required= False)
    biology = forms.IntegerField(min_value=0, max_value = 100,label='Biology', required= False)
    english = forms.IntegerField(min_value=0, max_value = 100, label='English', required= False)