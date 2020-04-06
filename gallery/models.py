from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=125)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption