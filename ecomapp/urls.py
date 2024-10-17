from django.contrib import admin
from django.urls import path, include
from ecomapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='index'),
    path("login",views.login,name='login'),
    path("home",views.home,name='home'),
   

]