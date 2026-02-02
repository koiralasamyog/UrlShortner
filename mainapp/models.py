# mainapp/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ShortURL(models.Model):
    original_url = models.URLField(max_length=500)
    short_url = models.CharField(max_length=10, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shorturls')
    time_date_created = models.DateTimeField(default=timezone.now)
    click_count = models.PositiveIntegerField(default=0)
    expiration_date = models.DateTimeField(null=True, blank=True)  # optional expiration

    def __str__(self):
        return f"{self.short_url} -> {self.original_url}"
