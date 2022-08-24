from email.errors import MalformedHeaderDefect
from pyexpat import model
from django.db import models

# Home Page

class AboutUs(models.Model):
    text = models.TextField()

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

    def __str__(self):
        return self.text[0:10]


class Services(models.Model):
    img = models.ImageField()
    service_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
    
    def __str__(self):
        return self.service_name[0:10]


class Announcements(models.Model):
    file = models.FileField()

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
    
    def __str__(self):
        return self.file


class Contacts(models.Model):
    dejurniy = models.CharField(max_length=155)
    buhgalteriya = models.CharField(max_length=155)
    telegram = models.CharField(max_length=155)

    email = models.EmailField()
    location = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"
        

class Requisites(models.Model):
    bank = models.CharField(max_length=255)
    RS = models.CharField(max_length=255)
    INN = models.CharField(max_length=155)
    OKOHX = models.CharField(max_length=255)
    OKED = models.CharField(max_length=255) 

    class Meta:
        verbose_name = "Реквизиты"
        verbose_name_plural = "Реквизиты"


# About Us Page


class AboutUsImg(models.Model):
    img = models.ImageField()
    sub_text = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.sub_text


class History(models.Model):
    text = models.TextField()
    img = models.ManyToManyField(AboutUsImg)

    class Meta:
        verbose_name = "История"
        verbose_name_plural = "История"

    def __str__(self):
        return self.text[0:15]


# ????? Primenenie fototexniki...


class Heros(models.Model):
    img = models.ImageField()

    class Meta:
        verbose_name = "Герои Топографы"
        verbose_name_plural = "Герои Топографы"

    def __str__(self):
        return self.img


class images(models.Model):
    img = models.ImageField()

class AboutUsMore(models.Model):
    header = models.CharField(max_length=255)
    images = models.ManyToManyField(images)

    class Meta:
        verbose_name = "О нас доп. информация"
        verbose_name_plural = "О нас доп. информация"

    def __str__(self):
        return self.header




# class ContactUs(models.Model):
#     name = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=155)
#     message = models.TextField()


# class SendEmailModel(models.Model):
#     fullname = models.CharField(max_length=255)
#     email = models.EmailField()
#     message = models.TextField()

#     class Meta:
#         verbose_name = 'Отправленные емейлы'
#         verbose_name_plural = 'Отправленные емейлы'

#     def __str__(self):
#         return self.fullname

