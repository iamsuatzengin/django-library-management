from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('book-list/', views.BookListView.as_view(), name="book_list"),
    path('book-detail/<int:id>', views.book_detail, name="book_detail"),
    path('author-list/', views.AuthorListView.as_view(), name="author_list"),
    path('author-detail/<int:id>', views.author_detail, name="author_detail"),
    path('search', views.search, name="search"),

    #CRUDs
    path('add-book/', views.add_book, name="add_book"),
    path('delete-book/<int:id>', views.delete_book, name="delete_book"),
    path('update-book/<int:id>', views.update_book, name="update_book"),

    path('add-author', views.add_author, name="add_author"),
    path('delete-author/<int:id>', views.delete_author, name="delete_author"),
    path('update-author/<int:id>', views.update_author, name="update_author"),

]
