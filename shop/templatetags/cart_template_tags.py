from django import template
from shop.models import Order

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        books = Order.objects.filter(user=user, ordered=False)
        if books.exists():
            return books[0].items.count()
    return 0
