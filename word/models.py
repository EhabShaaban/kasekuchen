from django.db import models

class Word(models.Model):
    
    string = models.CharField(max_length=100)
    length = models.IntegerField()
    language = models.CharField(max_length=2)
    data_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.string