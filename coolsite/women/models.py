from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, unique=True, db_index= True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Содержание')
    photo = models.ImageField(upload_to="photo/%Y/%m/%d", verbose_name='Фотокарточка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время внесения правок')
    is_published = models.BooleanField(default=True, verbose_name='Произведна ли публикация')
    cat = models.ForeignKey('Categories', on_delete=models.PROTECT, verbose_name='Категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts', kwargs={'post_slug':self.slug})

    class Meta:
        verbose_name='Известные женщины'
        verbose_name_plural='Известные женщины' #Изменение названия Womens на Известные женщины
        ordering = ['id', 'title'] #сортировка данных в админпанели таблицы Известные женщины



class Categories(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование категории')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug':self.slug})

    class Meta:
        verbose_name = 'Категория профессий женщин'
        verbose_name_plural = 'Категории профессий женщин'
        ordering = ['id', 'name']







