from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    ########### ceo ###########
    path('', views.wait, name="wait"),
    path('wait', views.wait, name="wait"),
    path('loading', views.loading, name="loading"),
    path('checking', views.checking, name="checking"),
    ########### customer ###########
    path('main1', views.main1, name="main1"),
    path('goods', views.goods, name="goods"),
    path('complete', views.complete, name="complete"),
    path('end', views.end, name="end"),
]