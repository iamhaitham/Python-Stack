from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('destroy_session',views.destroy),
    path('increment_by_2',views.increment_by_2),
    path('choose_increment_value',views.choose_increment_value),
]