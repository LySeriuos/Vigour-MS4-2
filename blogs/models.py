from django.db import models

# Create your models here.


class Blogs(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
