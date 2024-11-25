from django.contrib.auth import get_user_model
from django.db.models import ForeignKey, CharField, Model, CASCADE

YamDbUser = get_user_model()


class Review(Model):
    author = ForeignKey(YamDbUser, on_delete=CASCADE, related_name='reviews')


class Comment(Model):
    title = CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'