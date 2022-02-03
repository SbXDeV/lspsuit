from django.db import models


# Create your models here.
class Meeting(models.Model):
    """Модель отзывов"""
    photo = models.ImageField(upload_to='media/', verbose_name='Фото пользователя')
    username = models.CharField(max_length=30, verbose_name='Ф.И.О')
    company = models.CharField(max_length=30, verbose_name='Название компании')
    city = models.CharField(max_length=30, verbose_name='Город')
    description = models.TextField(max_length=340, verbose_name='Описание')
    star = models.IntegerField(verbose_name='Колличество звездочек', default=5)

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return 'Отзыв от пользователя: ' + self.username


class Event(models.Model):
    """ Модель отчета с мероприятий"""
    Events = [
        ('Weddings', 'Свадьбы'),
        ('Corporate', 'Корпоративы'),
        ('Team', 'Тимбилдинги'),
        ('presentations', 'Презентации'),
        ('conference', 'Конференции'),
        ('child', 'Детские мероприятия'),
        ('concert', 'Концерты')
    ]
    image = models.ImageField(upload_to='media/', verbose_name='Фото мероприятия')
    subclass = models.CharField(max_length=100, choices=Events, verbose_name='Какого типа мероприятие?')
    title = models.CharField(max_length=200, verbose_name='Название мероприятия')
    description = models.TextField(max_length=300, verbose_name='Краткое описание')

    class Meta:
        verbose_name = 'отчет с мероприятия'
        verbose_name_plural = 'Отчеты с мероприятий'

    def __str__(self):
        return 'Отчет с мероприятия: ' + self.title


class Profile(models.Model):
    image = models.ImageField(upload_to='media/', verbose_name='Фото сотрудника')
    first_name = models.CharField(max_length=100, verbose_name='Имя сотрудника')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия сотрудника')
    job = models.CharField(max_length=100, verbose_name='Должность')
    social_vk = models.CharField(max_length=100, verbose_name='Ссылка на вк')
    social_inst = models.CharField(max_length=100, verbose_name='Ссылка на инстаграм')

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'список сотрудников'

    def __str__(self):
        return 'Сотрудник: ' + self.first_name + ' ' + self.last_name


class Deca1(models.Model):
    image = models.ImageField(upload_to='media/', verbose_name='Фото блока')
    subtitle = models.CharField(max_length=100, verbose_name='Подзаголовок')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    desk = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Блок описания (верхний)'
        verbose_name_plural = 'блоки описания (верхний)'

    def __str__(self):
        return 'блок: ' + self.title


class Deca2(models.Model):
    image = models.ImageField(upload_to='media/', verbose_name='Фото блока')
    subtitle = models.CharField(max_length=100, verbose_name='Подзаголовок')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    desk = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Блок описания (нижний)'
        verbose_name_plural = 'блоки описания (нижний)'

    def __str__(self):
        return 'блок: ' + self.title


class Trust(models.Model):
    image = models.ImageField(upload_to='media/', verbose_name='Фото компании')

    class Meta:
        verbose_name = 'Компании которые нам доверяют'
        verbose_name_plural = 'Компании которые нам доверяют'

    def __str__(self):
        return 'Логотип: ' + self.image.name
