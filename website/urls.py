from django.urls import path
from . import views
app_name='website'


urlpatterns = [
 path('',views.index),
 path('register',views.register,name='register'),
 path('login',views.login,name='login'),
 path('home/<int:id>',views.home,name='home'),
 path('update/<int:id>',views.update,name='update'),
 path('changePass/<int:id>',views.changePass,name='changePass'),
 path('logout',views.logout,name='logout'),
 path('product',views.product,name='product'),
 path('productdetails/<int:id>',views.productdetails,name='productdetails')
 
 ]