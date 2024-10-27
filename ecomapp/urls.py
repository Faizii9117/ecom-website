from django.urls import path
from .views import index, register, auth_login_view, logout_view, contact
from .views import details_oneplus, details_samsung, details_realme, details_apple, details_vivo, details_oppo

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', auth_login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('contact/', contact, name='contact'),
    path('details/oneplus/', details_oneplus, name='details_oneplus'),
    path('details/samsung/', details_samsung, name='details_samsung'),
    path('details/realme/', details_realme, name='details_realme'),
    path('details/apple/', details_apple, name='details_apple'),
    path('details/vivo/', details_vivo, name='details_vivo'),
    path('details/oppo/', details_oppo, name='details_oppo'),
]
