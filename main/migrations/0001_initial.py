# Generated by Django 3.0.5 on 2020-04-03 16:32

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
            name='AppInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_app', models.CharField(max_length=200, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Информация о приложении',
                'verbose_name_plural': 'Информация о приложениях',
            },
        ),
        migrations.CreateModel(
            name='LoginPasswordInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100, unique=True)),
                ('appinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.AppInfo')),
            ],
            options={
                'verbose_name': 'Информация о логине и пароле',
                'verbose_name_plural': 'Информация о логинах и паролях',
            },
        ),
    ]