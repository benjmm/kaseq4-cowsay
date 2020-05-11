from django.shortcuts import render, reverse, HttpResponseRedirect
from django.utils import timezone

from appcowsay.models import Moo
from appcowsay.forms import FormAddMoo


def index(request):
    html = "index.html"
    if request.method == "POST":
        form = FormAddMoo(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Moo.objects.create(
                text=data['text'],
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = FormAddMoo()

    return render(request, html, {"form": form})


def errorview(request):
    html = "error.html"
    return render(request, html)


def historyview(request):
    html = "history.html"
    moos = Moo.objects.filter(
        date__lte=timezone.now()).order_by('date')
    return render(request, html, {'moos': moos})
