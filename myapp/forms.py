from django import forms
from django.forms import ModelForm
from myapp.models import Venue,Event
class Myform(forms.ModelForm):
    class Meta:
        model=Venue
        fields=['name','phone','address','email_address']

class Eventform(forms.ModelForm):
    class Meta:
        model=Event
        fields=['name','event_date','venue','manager']