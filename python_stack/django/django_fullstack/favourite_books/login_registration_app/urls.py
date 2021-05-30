from django.urls import path
from . import views 

app_name="login_registration_app"

urlpatterns = [
    path('',views.root,name="homepage"),
    path('registrationProcess',views.registrationProcess,name="registration"),
    path('success',views.success,name="success"),
    path('loginProcess',views.loginProcess,name="login"),
    path('logout',views.logout,name="logout"),
]
