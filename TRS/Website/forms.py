from pyexpat import model
from attr import field
from django import forms
from django.db import ModelForms
from .models import school_forms

class school_forms(ModelForms):
    class Meta:
        model = school_forms
        field = ('測試1' , '測試2' , '測試3' , '測試4')
