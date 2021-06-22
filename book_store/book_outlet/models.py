from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100) #or can put blank=True to allow blank entries in the field. Not allowed by default.
    is_bestselling_book = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True) # Harry Potter 1 => harry-potter-1

    # id = models.AutoField()  Can be used to increment but not needed. Automatically done.

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self): # method exists for every class in python. Can be overriden for changes to display
        return f"{self.title} ({self.rating})"