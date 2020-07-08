from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.utils import timezone

from .models import Book, OrderItem, Order


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


def add_to_cart(request, slug):
    book = get_object_or_404(Book, slug=slug)
    order_book, created = OrderItem.objects.get_or_create(
        item=book,
        user=request.user,
        ordered=False
    )
    order_queriset = Order.objects.filter(user=request.user, ordered=False)
    if order_queriset.exists():
        order = order_queriset[0]
        if order.items.filter(item__slug=book.slug).exists():
            order_book.quantity += 1
            order_book.save()
        else:
            order.items.add(order_book)
    else:
        order_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=order_date)
        order.items.add(order_book)
    return redirect('shop:book', slug=slug)
