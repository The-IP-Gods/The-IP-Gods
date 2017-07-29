from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='#', required=False, max_length=100)
    keywords = forms.CharField(label='Keywords', required=False, max_length=100)
    email = forms.EmailField(label='Email', required=False)
