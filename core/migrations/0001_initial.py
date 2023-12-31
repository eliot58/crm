# Generated by Django 4.1.6 on 2023-10-18 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_point', models.CharField(max_length=256, verbose_name='Название торговой точки')),
                ('fullName', models.CharField(max_length=256, verbose_name='ФИО')),
                ('address', models.CharField(blank=True, max_length=500, null=True, verbose_name='Адрес')),
                ('region', models.CharField(max_length=256, verbose_name='Регион')),
                ('director_phone', models.CharField(max_length=256, verbose_name='Телефон собственника')),
                ('manager_phone', models.CharField(blank=True, max_length=256, null=True, verbose_name='Телефон менеджера')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('with_work', models.CharField(blank=True, max_length=600, null=True, verbose_name='С кем работает')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='Фото')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('is_potential', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Общая база',
                'verbose_name_plural': 'Общая база',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'История обращений',
                'verbose_name_plural': 'История обращений',
            },
        ),
    ]
