from django.db import models
from api import choices


class Message(models.Model):
    fio = models.CharField(
        max_length=50,
        verbose_name="F.I.O"
    )
    phone = models.CharField(
        max_length=13,
        verbose_name="Telefon raqam"
    )
    message = models.TextField(
        verbose_name="Xabar"
    )
    status = models.CharField(
        max_length=50,
        choices=choices.MessageStatuses.choices,
        default=choices.MessageStatuses.YANGI
    )

    class Meta:
        verbose_name_plural = "1.Xabarlar"


class New(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name="Sarlavha"
    )
    description = models.TextField(
        verbose_name="Ma'lumot"
    )
    photo = models.ImageField(
        upload_to='news/',
        verbose_name="Rasm"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Vaqt"
    )

    class Meta:
        verbose_name_plural = "2.Yangiliklar"


class Management(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Ism va lavozim"
    )
    description = models.TextField(
        verbose_name="Ma'lumot"
    )
    photo = models.ImageField(
        upload_to='managements/',
        verbose_name="Rasm"
    )

    class Meta:
        verbose_name_plural = "3.Rahbariyat"


class Employee(models.Model):
    fio = models.CharField(
        max_length=50,
        verbose_name="F.I.O"
    )
    position = models.CharField(
        max_length=50,
        verbose_name="Lavozim"
    )
    status = models.CharField(
        max_length=100,
        verbose_name="Turi",
        choices=choices.EmployeeStatuses.choices
    )
    photo = models.ImageField(
        upload_to='students/',
        verbose_name="Rasm"
    )
    description = models.TextField(
        verbose_name="Ma'lumot",
        default=''
    )

    class Meta:
        verbose_name_plural = "4.Xodimlar"


class Event(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Sarlavha"
    )
    description = models.TextField(
        verbose_name="Ma'lumot",
        default=''
    )
    photo = models.ImageField(
        upload_to='events/',
        verbose_name="Rasm"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Vaqt"
    )

    class Meta:
        verbose_name_plural = "5.Tadbirlar"
        

class GuestLecture(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Sarlavha"
    )
    description = models.TextField(
        verbose_name="Ma'lumot",
        default=''
    )
    photo = models.ImageField(
        upload_to='events/',
        verbose_name="Rasm"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Vaqt"
    )

    class Meta:
        verbose_name_plural = "6.Mehmon ma'ruzalari"



