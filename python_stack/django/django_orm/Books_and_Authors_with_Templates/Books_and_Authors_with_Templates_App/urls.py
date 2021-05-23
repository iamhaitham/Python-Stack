from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('add_book',views.add_book),
    path('books/<int:number>',views.books),
    path('authors',views.authors),
    path('add_author',views.add_author),
    path('author/<int:Num>',views.some_author),
    path('assign_book',views.assign_book),
    path('some_book',views.some_book),
]
