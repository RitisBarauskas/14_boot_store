from django.db.models import CharField, Model


class Comment(Model):
    title = CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
