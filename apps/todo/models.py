from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название',
        unique=True
    )
    description = models.CharField(
        max_length=300,
        verbose_name="Описание",
        blank=True, null=True
    )
    is_completed = models.BooleanField(
        verbose_name="Статус",
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фотография сайта'
    )


    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = "Таски"
        verbose_name_plural = "Таски"