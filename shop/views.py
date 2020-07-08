from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

# def item_list(request):
#     context = {
#         'book': Book.objects.all()
#     }
#     return render(request, 'item_list.html', context)

def checkout(request):
    return render(request, 'checkout.html')

# def home(request):
#     context = {
#         'books': Book.objects.all()
#     }
#     return render(request, 'home.html', context)

class HomeView(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'
    ordering = ['-date_posted']
    paginate_by = 8