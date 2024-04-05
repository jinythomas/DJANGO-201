from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length=240)
    date = models.DateTimeField(auto_now=True) # auto_now makes the date field non editable

    def __str__(self):
        return self.text[0:100]
