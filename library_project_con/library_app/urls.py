from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('book-list/', views.BookListView.as_view(), name="book_list"),
    path('book-detail/<int:id>', views.book_detail, name="book_detail"),
]
