from django.db import models
from django.urls import reverse


class Sections(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название раздела")
    image_link = models.TextField(null=True, verbose_name="URL картинки")
    description = models.TextField(max_length=100, null=True, verbose_name="Описание")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовать")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('section', kwargs={'section_slug': self.slug})

    class Meta:
        verbose_name = 'Разделы'
        verbose_name_plural = 'Разделы'
