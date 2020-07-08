from django.shortcuts import render

from .models import Book

def item_list(request):
    context = {
        'book': Book.objects.all()
    }
    return render(request, 'item_list.html', context)
