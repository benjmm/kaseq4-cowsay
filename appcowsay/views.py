from django.shortcuts import render, reverse, HttpResponseRedirect
from django.utils import timezone

from appcowsay.models import Moo
from appcowsay.forms import FormAddMoo


def index(request):
    html = 'index.html'
    if request.method == 'POST':
        form = FormAddMoo(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Moo.objects.create(
                text=data['text'],
            )
            # return HttpResponseRedirect(reverse('homepage'))
            return render(request, html, {'form': FormAddMoo,
                                          'moo': data['text']})

    form = FormAddMoo()

    return render(request, html, {'form': form})


def errorview(request):
    html = 'error.html'
    return render(request, html)


def historyview(request):
    html = 'history.html'
    # last = Moo.objects.all().count()
    # moos = Moo.objects.all()[(last-3):last].order_by('-date')
    moos = Moo.objects.order_by('-date')[:10]
    return render(request, html, {'moos': moos})
