from django.db import models
from django.db.models.fields import TextField
from django.shortcuts import reverse
from ckeditor.fields import RichTextField


class Blog(models.Model):

    LANGUAGES_CHOICES = (
    ('python', 'P'),
    ('django', 'D'),
    ('javascript', 'J'),
    ('react', 'R'),
    ('other', 'O'),
    )

    title = models.CharField(max_length=50)
    description = TextField(max_length=200)
    body = RichTextField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGES_CHOICES, max_length=50)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        """ Return a string representation of Blog """
        return self.title

    def get_absolute_url(self):
        return reverse("core:posts", kwargs={"slug": self.slug})

    def get_language_url(self):
        return reverse("core:language", kwargs={"language": self.language})
    