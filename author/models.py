from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User,
                                verbose_name=_('user'),
                                on_delete=models.CASCADE,
                                related_name='author')
    phone_number = models.CharField(verbose_name=_('phone number'),
                                    max_length=11)
    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')
        db_table = 'Author'
