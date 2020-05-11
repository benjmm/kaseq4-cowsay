from django.shortcuts import render, reverse, HttpResponseRedirect

# from appcowsay.models import Moo
# from appcowsay.forms import Addmoo


def index(request):
    html = "index.html"
    return render(request, html)


def errorview(request):
    html = "error.html"
    return render(request, html)


def historyview(request):
    html = "history.html"
    return render(request, html)
