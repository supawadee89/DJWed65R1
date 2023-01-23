from django.urls import path
from ProfileApp import views

urlpatterns = [

    path('test/', views.test, name='test'),
    path('firstweb/', views.firstweb, name='firstweb'),
    path('secondpage/', views.secondpage, name='secondpage'),
    path('thirdpage/', views.thirdpage, name='thirdpage'),
    path('header/', views.header, name='header'),
    path('rolemodel/', views.rolemodel, name='rolemodel'),
    path('showMyData/', views.showMyData, name='showMyData'),
    path('showProduct/', views.showProduct, name='showProduct'),
    path('newProduct/', views.newProduct, name='newProduct'),
    path('frmProduct/', views.frmProduct, name='frmProduct'),

    ]
