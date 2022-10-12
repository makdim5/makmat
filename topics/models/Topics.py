from ckeditor.fields import RichTextField

from django.db import models
from django.urls import reverse


class Topics(models.Model):
    topic_name = models.CharField(max_length=255, verbose_name="Название темы")
    content = RichTextField(null=True, verbose_name="Текст лекции")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовать")
    section = models.ForeignKey('Section', on_delete=models.PROTECT, null=True, verbose_name="Выбор раздела")
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def get_absolute_url(self):
        return reverse('topic', kwargs={'topic_slug': self.slug})

    def __str__(self):
        return self.topic_name

    class Meta:
        verbose_name = 'Темы'
        verbose_name_plural = 'Темы'
        ordering = ['section', 'time_create']
