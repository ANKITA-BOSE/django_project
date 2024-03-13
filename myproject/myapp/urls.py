from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about-page'),
    path('client', views.client, name='client-page'),
    path('contact', views.contact, name='contact-page'),
    path('index', views.index, name='index-page'),
    path('products', views.products, name='products-page'),
    path('reg/', views.userReg, name='reg-page'),
]