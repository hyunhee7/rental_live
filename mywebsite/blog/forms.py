from django import forms

class info(forms.Form):
    user_id = forms.CharField(label='user_id')
