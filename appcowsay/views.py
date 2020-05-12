from django.shortcuts import render
import subprocess

from appcowsay.models import Moo
from appcowsay.forms import FormAddMoo


def transform(rawmoo):
    result = rawmoo.decode('utf-8')
    return result


def index(request):
    html = 'index.html'
    if request.method == 'POST':
        form = FormAddMoo(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data['text']
            cow = data['cow']
            Moo.objects.create(
                text=text,
                cow=cow)
            moo = subprocess.check_output(
                ["cowsay", '-f', cow, text]).decode('utf-8')
            return render(request, html, {'form': FormAddMoo,
                                          'moo': moo})

    form = FormAddMoo()

    return render(request, html, {'form': form})


def errorview(request):
    html = 'error.html'
    return render(request, html)


def historyview(request):
    html = 'history.html'
    moos = Moo.objects.order_by('-date')[: 10]
    return render(request, html, {'moos': moos})
