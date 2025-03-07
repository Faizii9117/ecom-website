from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ecomapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    
    path('admin/', admin.site.urls),
    path("",views.index,name='index'),
    path("login/", views.auth_login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
    path('contact/', views.contact_view, name='contact'),  # Match the `redirect` call
    path("buynow/", views.product_view, name='product'),
    path("paynow/", views.paynow, name='paynow'),
    path("register/",views.register,name="register"),
    path("details-samsung/",views.details_samsung,name="details"),
    path("details-oneplus/",views.details_oneplus,name="details"),
    path("details-realme/",views.details_realme,name="details"),
    path("details-apple/",views.details_apple,name="details"),
    path("details-vivo/",views.details_vivo,name="details"),
    path("details-oppo/",views.details_oppo,name="details"),
    path("products/", views.products, name="products"),
    path("index/", views.index, name="index"),
    

   

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)