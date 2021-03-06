from django.db import models


class Trainers(models.Model):
    trainer_name = models.CharField(max_length=254)
    trainer_about = models.CharField(max_length=254, null=True, blank=True)
    program1 = models.CharField(max_length=254, null=True, blank=True)
    program2 = models.CharField(max_length=254)
    program3 = models.CharField(max_length=254, null=True, blank=True)
    trainer_highlight = models.TextField(null=True, blank=True)
    trainer_text = models.TextField(null=True, blank=True)
    trainer_text_hidden = models.TextField(null=True, blank=True)
    trainer_goals = models.TextField(max_length=254, null=True, blank=True)
    trainer_image_url = models.URLField(max_length=1024)
    image = models.ImageField(null=True, blank=True)
        
    def __str__(self):
        return self.trainer_name
