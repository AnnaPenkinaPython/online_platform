# Generated by Django 4.2.3 on 2023-07-12 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_owner_lesson_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='owner',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='owner',
            new_name='user',
        ),
    ]