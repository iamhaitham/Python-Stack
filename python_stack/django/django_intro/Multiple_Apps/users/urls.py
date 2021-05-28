from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register, name="users_register"),
    path('login',views.login, name="users_login"),
    path('users',views.users, name="users"),
    path('users/new',views.users_new, name="users_new"),
    path('',views.root_route,name="root_route"),
]
