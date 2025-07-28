from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField( auto_now=True)


    def __str__(self):
        return self.title




