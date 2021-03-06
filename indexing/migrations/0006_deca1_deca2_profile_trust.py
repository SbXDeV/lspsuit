# Generated by Django 3.2.9 on 2022-02-02 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexing', '0005_auto_20211118_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deca1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Фото блока')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Подзаголовок')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('desk', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Блок описания',
                'verbose_name_plural': 'блоки описания',
            },
        ),
        migrations.CreateModel(
            name='Deca2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Фото блока')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Подзаголовок')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('desk', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Блок описания',
                'verbose_name_plural': 'блоки описания',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Фото сотрудника')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя сотрудника')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия сотрудника')),
                ('job', models.CharField(max_length=100, verbose_name='Должность')),
                ('social_vk', models.CharField(max_length=100, verbose_name='Ссылка на вк')),
                ('social_inst', models.CharField(max_length=100, verbose_name='Ссылка на инстаграм')),
            ],
            options={
                'verbose_name': 'сотрудник',
                'verbose_name_plural': 'список сотрудников',
            },
        ),
        migrations.CreateModel(
            name='Trust',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Фото компании')),
            ],
        ),
    ]
