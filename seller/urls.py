from django.urls import path,include
from . import views

urlpatterns = [
    path('sellerindex/',views.sellerindex,name='sellerindex'),
    path('',views.sellerlogin,name='sellerlogin'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('manageproduct/',views.manageproduct,name='manageproduct'),
    path('editproduct/<int:pid>',views.editproduct,name='editproduct'),
    path('deleteproduct/<int:pid>',views.deleteproduct,name='deleteproduct')
]