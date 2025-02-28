from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.BigIntegerField()
    created_at = models.DateField(auto_now_add=True)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",
        blank=True
    )
    
    def __str__(self):
        return self.username

class Activity(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    action = models.CharField(max_length=255)
    timestamp = models.DateField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['timestamp'])
        ]
        ordering = ['-timestamp']
        
    def __str__(self):
        return f"{self.user.username} - {self.action}"