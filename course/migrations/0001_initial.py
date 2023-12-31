# Generated by Django 4.2.3 on 2023-07-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='', verbose_name='превью')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='', verbose_name='превью')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('video', models.CharField(blank=True, max_length=150, null=True, verbose_name='ссылка на видео')),
            ],
        ),
    ]