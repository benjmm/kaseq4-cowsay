from django.urls import path

from appcowsay import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('error/', views.errorview, name='errorpage'),
    path('history/', views.historyview, name='historypage'),
]
