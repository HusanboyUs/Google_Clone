from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.homePage, name='homepage'),
    path('result/',views.viewPage, name='result'),
]
