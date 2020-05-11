from django import forms
from appcowsay.models import Moo


class FormAddMoo(forms.ModelForm):
    class Meta:
        model = Moo
        fields = [
            'text'
        ]
