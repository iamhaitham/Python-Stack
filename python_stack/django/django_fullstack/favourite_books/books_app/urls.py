from django.urls import path
from . import views 

app_name="books_app"

urlpatterns = [
    path('',views.root,name="books_homepage"),
    path('add_books',views.add_books,name="books_add"),
    path('favourite_this/<int:book_id>',views.favourite_this,name='favourite_this'),
    path('<int:book_id>',views.bookinfo,name="book_info"),
    path('unfavourite_this/<int:book_id>',views.unfavourite_this),
    path('update_book/<int:book_id>',views.update_book),
    path('delete/<int:book_id>',views.delete)
]