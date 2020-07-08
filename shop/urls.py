from django.urls import path
from .views import HomeView, BookDetailView, checkout, add_to_cart

app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='books-list'),
    path('book/<str:slug>/', BookDetailView.as_view(), name='book'),
    path('checkout/', checkout, name='checkout'),
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart'),

]