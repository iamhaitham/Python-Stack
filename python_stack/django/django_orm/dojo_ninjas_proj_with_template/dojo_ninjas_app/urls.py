from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('Dojo',views.Dojo),
    path('Ninja',views.Ninja),
    path('Delete',views.Delete),
]
