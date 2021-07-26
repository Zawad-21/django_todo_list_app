from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=1000, null=True, verbose_name="")
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title