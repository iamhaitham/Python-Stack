from django.urls import path
from . import views 

urlpatterns = [
    path('',views.root),
    path('registrationProcess',views.registrationProcess),
    path('success',views.success),
    path('loginProcess',views.loginProcess),
    path('logout',views.logout),
]
