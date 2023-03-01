from django.db import models

# Create your models here.


class Album(models.Model):
    # our Album class is inheriting from Django's
    # model class, located in models/
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.artist}'
