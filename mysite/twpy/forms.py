from django import forms

class TwForm(forms.Form):
    screen_name = forms.CharField(label='name')
