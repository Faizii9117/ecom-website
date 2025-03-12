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
    path("register/",views.register,name="register"),
    path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
    path("index/", views.index, name="index"),
    path('item/',views.item, name='item '),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('product_detail/<int:id>/buynow/', views.buy_now, name='buynow'),
    # path('product/buy/<int:id>/', views.product_detail_1, name='product_detail'),



    

   

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)