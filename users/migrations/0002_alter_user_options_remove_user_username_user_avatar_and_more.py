# Generated by Django 5.1.1 on 2024-09-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to="users/avatars", verbose_name="Аватар"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="chat_id",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="chat_id"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="city",
            field=models.CharField(
                blank=True, max_length=25, null=True, verbose_name="Город"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True, max_length=25, null=True, verbose_name="Телефон"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True, verbose_name="Почта"),
        ),
    ]
