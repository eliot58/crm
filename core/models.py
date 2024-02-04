from django.db import models
from django.contrib.auth.models import User

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




class Log(models.Model):
    manager = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    datetime = models.DateTimeField(auto_now_add = True)
    comment = models.TextField(null = True, blank = True, verbose_name = "Комментарий")


    def __str__(self) -> str:
        return f"{self.datetime} {self.comment} {self.manager.username}"


    class Meta:
        verbose_name = "История обращений"
        verbose_name_plural = "История обращений"

