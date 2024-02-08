from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Client(models.Model):
    name_point = models.CharField(max_length = 256, verbose_name = "Название торговой точки")
    fullName = models.CharField(max_length = 256, verbose_name = "ФИО")
    address = models.CharField(max_length = 500, null = True, blank = True, verbose_name = "Адрес")
    region = models.CharField(max_length = 256, verbose_name = "Регион")
    director_phone = models.CharField(max_length = 256, verbose_name = "Телефон собственника")
    manager_phone = models.CharField(max_length = 256, null = True, blank = True, verbose_name = "Телефон менеджера")
    email = models.EmailField(null = True, blank = True, verbose_name = "Email")
    with_work = models.CharField(max_length = 600, null = True, blank = True, verbose_name = "С кем работает")
    photo = models.ImageField(upload_to = "photo", null = True, blank = True, verbose_name = "Фото")
    is_potential = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.name_point


    class Meta:
        verbose_name = "База"
        verbose_name_plural = "База"


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length = 20)


    def __str__(self) -> str:
        return self.user.username


    class Meta:
        verbose_name = "Менеджер"
        verbose_name_plural = "Менеджеры"


class Calculator(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length = 20)


    def __str__(self) -> str:
        return self.user.username


    class Meta:
        verbose_name = "Расчетчик"
        verbose_name_plural = "Расчетчики"


class File(models.Model):
    file = models.FileField(upload_to="calc_info")


class Log(models.Model):
    manager = models.ForeignKey(Manager, on_delete = models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    datetime = models.DateTimeField(auto_now_add = True)
    comment = models.TextField(null = True, blank = True, verbose_name = "Комментарий")
    file = models.OneToOneField(File, on_delete = models.DO_NOTHING, null = True, blank = True)


    def __str__(self) -> str:
        if self.file:
            return f"{self.datetime} {self.comment} <a style='color: #c3ff53; font-weight: 500;' href='{self.file.file.url}'>Файл</a> {self.manager.user.username}"
        return f"{self.datetime} {self.comment} {self.manager.user.username}"


    class Meta:
        verbose_name = "История обращений"
        verbose_name_plural = "История обращений"


    

