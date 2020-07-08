from django.urls import path
from .views import HomeView, checkout

app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='books-list'),
    path('checkout/', checkout, name='checkout'),

]