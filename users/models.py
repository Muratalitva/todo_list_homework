from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(
        max_length=255, 
        verbose_name='Имя',
        unique=True
    )
    email = models.EmailField(
        verbose_name='Email',
        unique=True
    )
    phone_number = models.CharField(
        max_length=12, 
        verbose_name='Телефонный номер',
        unique=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    age = models.IntegerField(
        verbose_name="Возраст"
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"