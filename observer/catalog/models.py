# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Genre(models.Model):
  name = models.CharField(max_length=200, 
                          help_text="Enter a article genre (e.g. news, funny)")

  def __str__(self):
    return self.name

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Article(models.Model):
  """
  Model representing a book (but not a specific copy of a book).
  """
  title = models.CharField(max_length=200)
  vender = models.ForeignKey('Vender', on_delete=models.SET_NULL, null=True)
  # Foreign Key used because book can only have one author, but authors can have multiple books
  # Author as a string rather than object because it hasn't been declared yet in the file.
  text = models.TextField(max_length=1000, help_text="Enter text")
  #isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
  genre = models.ManyToManyField(Genre, help_text="Select a genre for this text")
  # ManyToManyField used because genre can contain many books. Books can cover many genres.
  # Genre class has already been defined so we can specify the object above.
  
  def __str__(self):
    """
    String for representing the Model object.
    """
    return self.title
  
  
  def get_absolute_url(self):
    """
    Returns the url to access a particular book instance.
    """
    return reverse('book-detail', args=[str(self.id)])
