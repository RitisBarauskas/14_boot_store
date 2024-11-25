from django.contrib.auth import get_user_model
from django.db.models import Model, SlugField, CharField, ForeignKey, CASCADE, DateTimeField, TextField

from goods.constants import (
    MAX_LENGTH_SLUG_FIELD,
    MAX_LENGTH_CHAR_FIELD,
    MAX_LENGTH_DISPLAY_STR,
)

User = get_user_model()


class Category(Model):
    slug = SlugField(verbose_name='Слаг', max_length=MAX_LENGTH_SLUG_FIELD, unique=True)
    name = CharField(verbose_name='Имя', max_length=MAX_LENGTH_CHAR_FIELD)
    author = ForeignKey(User, verbose_name='Автор', on_delete=CASCADE, related_name='categories', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ('name',)

    def __str__(self):
        return self.name[:MAX_LENGTH_DISPLAY_STR]


class Good(Model):
    name = CharField(verbose_name='Имя', max_length=MAX_LENGTH_CHAR_FIELD)
    category = ForeignKey(Category, verbose_name='Категория', on_delete=CASCADE, related_name='goods')
    description = TextField(verbose_name='Описание', blank=True)
    created_at = DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = DateTimeField(verbose_name='Дата обновления', auto_now=True)
    creator = ForeignKey(User, verbose_name='Создатель', on_delete=CASCADE, related_name='goods', blank=True, null=True)
    moderator = ForeignKey(User, verbose_name='Модератор', on_delete=CASCADE, related_name='moderated_goods', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name[:MAX_LENGTH_DISPLAY_STR]
