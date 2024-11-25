from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import ForeignKey

YamDbUser = get_user_model()


class Review(models.Model):
    author = ForeignKey(YamDbUser, on_delete=models.CASCADE, related_name='reviews')
