# Generated by Django 4.1.6 on 2024-02-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='director_phone',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Телефон собственника'),
        ),
        migrations.AlterField(
            model_name='client',
            name='fullName',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name_point',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Название торговой точки'),
        ),
        migrations.AlterField(
            model_name='client',
            name='region',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Регион'),
        ),
    ]