from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('sproduct/<int:pid>',views.sproduct,name='sproduct'),
    
    path('allproduct/',views.allproduct,name='allproduct'),
    path('hardware/',views.hardware,name='hardware'),
    path('addtocart/',views.addtocart,name='addtocart'),
    path('cart/',views.cart,name='cart'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    #path('checkout/',views.checkout,name='checkout'),
    path('pay/',views.checkout,name='pay'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.service,name='service'),
    
]