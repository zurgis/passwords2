from django.db import models

from users.models import User

# Create your models here.
class AppInfo(models.Model):
    name_app = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Информация о приложениях'
        verbose_name = 'Информация о приложении'

    def __str__(self):
        return self.name_app

class LoginPasswordInfo(models.Model):
    appinfo = models.ForeignKey(AppInfo, on_delete=models.CASCADE)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Информация о логинах и паролях'
        verbose_name = 'Информация о логине и пароле'

    def __str__(self):
        return self.login