from django.db import models
from django.conf import settings

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
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    item = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.item


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    created = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

