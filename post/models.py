from django.db import models
from django.utils.translation import gettext_lazy as _
from author.models import Author


class Post(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=256)
    body = models.TextField(verbose_name=_('body'), null=True)
    image = models.ImageField(verbose_name=_('image'), upload_to='media')
    author = models.ForeignKey(Author,
                               on_delete=models.SET_NULL,
                               related_name='posts',
                               verbose_name=_('author'),
                               null=True)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        db_table = 'Post'