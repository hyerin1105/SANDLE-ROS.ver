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
    path('main', views.main, name="main"),
    path('goods/<int:customer_id>', views.goods, name="goods"),
    path('complete', views.complete, name="complete"),
    path('end', views.end, name="end"),
]