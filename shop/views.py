from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.contrib import messages

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
    order_queryset = Order.objects.filter(user=request.user, ordered=False)
    if order_queryset.exists():
        order = order_queryset[0]
        if order.items.filter(item__slug=book.slug).exists():
            order_book.quantity += 1
            order_book.save()
            messages.info(request, 'This book was again added to your cart')
        else:
            order.items.add(order_book)
            messages.info(request, 'This book was added to your cart')
    else:
        order_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=order_date)
        order.items.add(order_book)
        messages.info(request, 'This book was added to your cart')
    return redirect('shop:book', slug=slug)

def remove_from_cart(request, slug):
    book = get_object_or_404(Book, slug=slug)
    order_queryset = Order.objects.filter(
        ordered=False,
        user=request.user,
    )
    if order_queryset.exists():
        order = order_queryset[0]
        if order.items.filter(item__slug=book.slug).exists():
            order_book = OrderItem.objects.filter(
                item=book,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_book)
            messages.info(request, 'This book was delete from your cart')
            return redirect('shop:book', slug=slug)
        else:
            messages.info(request, 'This book was not in your cart')
            return redirect('shop:book', slug=slug)
    else:
        messages.info(request, "Yuo don't have order")
        return redirect('shop:book', slug=slug)

