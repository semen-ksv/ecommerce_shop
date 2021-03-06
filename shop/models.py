from django.db import models
from django.conf import settings
from django.utils import timezone
from django.shortcuts import reverse

GENRE_CHOICES = (
    ('A', 'Affairs'),
    ('C', 'Classic'),
    ('D', 'Detectives'),
    ('F', 'Fantastic'),
    ('M', 'Militants'),
)

LABEL_CHOICES = (
    ('D', 'danger'),
    ('P', 'primary'),
    ('S', 'secondary'),
)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField('Author', blank=True, related_name='book')
    genre = models.CharField(choices=GENRE_CHOICES, max_length=1)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    date_posted = models.DateField(default=timezone.now)
    price = models.FloatField()
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:book', kwargs={'slug': self.slug})

    def get_add_to_cart_url(self):
        return reverse('shop:add_to_cart', kwargs={'slug': self.slug})

    def get_remove_from_cart_url(self):
        return reverse('shop:remove_from_cart', kwargs={'slug': self.slug})


class Author(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    item = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.title}'

    def get_total_item_price(self):
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    created = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total

