from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

from datetime import date

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.caption}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True, 
        # default=date.today
        )
    slug = models.SlugField(unique=True, null=False, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])

    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return f"{self.title}, {self.date}"




