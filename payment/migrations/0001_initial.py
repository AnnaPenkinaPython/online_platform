# Generated by Django 4.2.3 on 2023-07-11 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0002_alter_lesson_options_lesson_course'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_payment', models.DateField(auto_now_add=True, verbose_name='дата оплаты')),
                ('payment_amount', models.IntegerField(verbose_name='сумма оплаты')),
                ('payment_method', models.CharField(choices=[('CASH', 'наличные'), ('TRANSFER_TO_ACCOUNT', 'перевод на счет')], max_length=50, verbose_name='способ оплаты')),
                ('paid_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='оплаченный курс')),
                ('paid_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.lesson', verbose_name='оплаченный курс')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'способ оплаты',
                'verbose_name_plural': 'способы оплаты',
            },
        ),
    ]