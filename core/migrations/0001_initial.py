# Generated by Django 4.1.6 on 2024-02-29 12:36

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
                ('name_point', models.CharField(default='', max_length=256, verbose_name='Название торговой точки')),
                ('fullName', models.CharField(default='', max_length=256, verbose_name='ФИО')),
                ('address', models.CharField(default='', max_length=500, verbose_name='Адрес')),
                ('region', models.CharField(default='', max_length=256, verbose_name='Регион')),
                ('director_phone', models.CharField(default='', max_length=20, unique=True, verbose_name='Телефон собственника')),
                ('manager_phone', models.CharField(default='', max_length=20, verbose_name='Телефон менеджера')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('with_work', models.CharField(default='', max_length=600, verbose_name='С кем работает')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='Фото')),
                ('refuse', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'База',
                'verbose_name_plural': 'База',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='calc_info')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcustomer', models.IntegerField()),
                ('c_name', models.CharField(max_length=256)),
                ('create_date', models.CharField(max_length=10)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('last_order_date', models.CharField(max_length=10)),
                ('manager', models.CharField(max_length=256)),
                ('manager_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('last_works_update', models.DateField(blank=True, null=True)),
                ('idpeople', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Менеджер',
                'verbose_name_plural': 'Менеджеры',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client')),
                ('file', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.file')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.manager')),
            ],
            options={
                'verbose_name': 'История обращений',
                'verbose_name_plural': 'История обращений',
            },
        ),
        migrations.AddField(
            model_name='client',
            name='potential',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.manager'),
        ),
        migrations.CreateModel(
            name='Calculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Расчетчик',
                'verbose_name_plural': 'Расчетчики',
            },
        ),
    ]
