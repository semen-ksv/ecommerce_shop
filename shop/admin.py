from django.contrib import admin

from .models import Book, OrderItem, Order, Author

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(OrderItem)
admin.site.register(Order)

