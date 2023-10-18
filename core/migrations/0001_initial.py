# Generated by Django 4.1.6 on 2023-10-18 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            ],
            options={
                'verbose_name': 'История обращений',
                'verbose_name_plural': 'История обращений',
            },
        ),
    ]