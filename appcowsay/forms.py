from django import forms
from appcowsay.helpers import cow_list


class FormAddMoo(forms.Form):
    text = forms.CharField(max_length=150)
    cow = forms.CharField(widget=forms.Select(choices=cow_list))
