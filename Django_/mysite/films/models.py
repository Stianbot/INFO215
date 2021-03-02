from django.db import models

# Create your models here.


class Film(models.Model):
    title = models.CharField(max_length=50)
    length = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.title