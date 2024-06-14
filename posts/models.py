from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=75)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title

    def serialize(self):
        return {
            'title': self.title,
            'body': self.body,
            'date': self.date,
            'slug': self.slug
        }
