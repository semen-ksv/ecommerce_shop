from django.urls import path
from .views import HomeView, BookDetailView, OrderView,\
    checkout, add_to_cart, remove_from_cart, remove_book_in_cart, add_in_cart

app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='books-list'),
    path('book/<str:slug>/', BookDetailView.as_view(), name='book'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', OrderView.as_view(), name='cart'),
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart'),
    path('add_in_cart/<slug>', add_in_cart, name='add_in_cart'),
    path('remove_from_cart/<slug>', remove_from_cart, name='remove_from_cart'),
    path('remove_book/<slug>', remove_book_in_cart, name='remove_book_in_cart'),


]