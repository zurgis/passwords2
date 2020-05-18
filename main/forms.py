from django import forms
from django.utils.crypto import get_random_string

from .models import AppInfo, LoginPasswordInfo

class AppLoginPasswordForm(forms.Form):
    """ A form for creating new appinfo and loginpasswordinfo """
    name_app = forms.CharField(max_length=200, label='Название приложения')
    login = forms.CharField(max_length=100, label='Логин')
    # get_random_string используем в качестве нового пароля по умолчанию 
    password = forms.CharField(max_length=50, label='Пароль', initial=get_random_string)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        super().__init__()
        name_app = self.cleaned_data.get('name_app')
        login = self.cleaned_data.get('login')
        password = self.cleaned_data.get('password')
        
        if not name_app or not login or not password:
            raise forms.ValidationError("Заполните все поля формы!")

    def save(self):
        name_app = self.cleaned_data.get('name_app')
        login = self.cleaned_data.get('login')
        password = self.cleaned_data.get('password')

        AppInfo.objects.get_or_create(name_app=name_app, user=self.user)
        # Получаем, только что созданный объект, для сохранения след. формы
        appinfo = AppInfo.objects.get(name_app=name_app)
        # Устанавливаем фильтрацию записей по логину, чтобы не было возможности
        # хранить в одном приложении одинаковые логины
        if LoginPasswordInfo.objects.filter(appinfo=appinfo, login=login).exists():
            raise forms.ValidationError('Такая запись сущесвует')  # НАПИСАТЬ ИСКЛЮЧЕНИЕ!!
        LoginPasswordInfo.objects.create(appinfo=appinfo, login=login, password=password)


class LoginPasswordForm(forms.ModelForm):
    class Meta:
        model = LoginPasswordInfo
        fields = ('login', 'password')