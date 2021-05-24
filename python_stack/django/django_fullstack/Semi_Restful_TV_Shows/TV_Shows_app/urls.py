from django.urls import path
from . import views

urlpatterns = [
    path('',views.root),
    path('shows',views.shows),
    path('shows/new',views.add_shows),
    path('create_shows',views.create_shows),
    path('shows/<int:number>',views.some_show),
    path('shows/<int:number>/edit',views.update_show),
    path('update',views.update_show_process),
    path('shows/<int:number>/delete',views.delete),
]