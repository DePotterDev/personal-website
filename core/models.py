from django.db import models

LANGUAGES_CHOICES = (
    ('P', 'Python'),
    ('D', 'Django'),
    ('J', 'JavaScript'),
    ('R', 'React.js'),
    ('O', 'other'),
)

class Blog(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    language = models.CharField(choices=LANGUAGES_CHOICES, max_length=50)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)