from django.contrib import admin
from django.urls import path, include
from ecomapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='index'),
    path("login/", views.auth_login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("contact/", views.contact, name='contact'),
    path("buynow/", views.buynow, name='buynow'),
    path("paynow/", views.paynow, name='paynow'),
    path("register/",views.register,name="register"),
    path("details-samsung/",views.details_samsung,name="details"),
    path("details-oneplus/",views.details_oneplus,name="details"),
    path("details-realme/",views.details_realme,name="details"),
    path("details-apple/",views.details_apple,name="details"),
    path("details-vivo/",views.details_vivo,name="details"),
    path("details-oppo/",views.details_oppo,name="details"),
   


   

]