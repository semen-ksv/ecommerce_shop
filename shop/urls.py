from django.urls import path
from .views import HomeView, BookDetailView, checkout

app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='books-list'),
    path('book/<str:slug>/', BookDetailView.as_view(), name='book'),
    path('checkout/', checkout, name='checkout'),

]