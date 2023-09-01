from django.urls import path, include
import main.views

urlpatterns = [
    path('', main.views.main, name="main"),
    path('goods', main.views.goods, name="goods"),
    path('complete', main.views.complete, name="complete"),
    path('end', main.views.end, name="end"),
]