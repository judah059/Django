from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=100, null=False, blank=False)
    lastname = models.CharField(max_length=100, null=False, blank=False)


class User(models.Model):
    firstname = models.CharField(max_length=100, null=False, blank=False)
    lastname = models.CharField(max_length=100, null=False, blank=False)


class Book(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    genre = models.CharField(max_length=50, null=False, blank=False)
    author = models.ManyToManyField(Author, related_name='books')
    user = models.ManyToManyField(User, default='Nobody took the book', related_name='user')
    availability = models.BooleanField(default=True)


# Create your models here.
