from django.contrib import admin
from django.urls import path, include
from ecomapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='index'),
    path("login/", views.auth_login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("contact/", views.contact, name='contact'),
    path("register/",views.register,name="register"),

   

]