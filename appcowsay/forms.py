from django import forms
import subprocess

cows = subprocess.check_output(
    ["cowsay", '-l']).decode('utf-8').split()[4:]
cow_list = list(zip(cows, cows))


class FormAddMoo(forms.Form):
    text = forms.CharField(max_length=150)
    cow = forms.CharField(widget=forms.Select(choices=cow_list))
