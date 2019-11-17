from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length = 20, help_text = "Tile for your note")
    description = models.TextField(max_length = 2000, help_text = "Description for your note")
    creation_date = models.DateField(auto_now_add=True, null=True)
    updation_date = models.DateField(auto_now=True, null=True)
    
    def __str__(self):
        return self.title