from django.urls import path
from . import views

urlpatterns = [
    path('',views.sign),
    path('wall',views.wall),
    path('registrationProcess',views.registrationProcess),
    path('loginProcess',views.loginProcess),
    path('success',views.success),
    path('message_process',views.message_process),
    path('comment_process',views.comment_process),
    path('delete_process',views.delete_process),
    path('logout',views.logout),
]
