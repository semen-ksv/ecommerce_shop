from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book


def checkout(request):
    return render(request, 'checkout.html')


class HomeView(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'
    ordering = ['-date_posted']
    paginate_by = 8

class BookDetailView(DetailView):
    model = Book
    template_name = 'book.html'
    context_object_name = 'book'

