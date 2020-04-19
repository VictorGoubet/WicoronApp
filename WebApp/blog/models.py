from django.db import models

# Create your models here.


class Posts(models.Model):
    #id defini automatiquement
    title=models.CharField(max_length=255)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    Modified_at=models.DateTimeField(auto_now=True)  
