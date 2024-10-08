from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'receiver')
    def __str__(self):
        return self.message
    
