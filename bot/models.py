from django.db import models


# Create your models here.


class Questionnaire(models.Model):
    class Meta:
        verbose_name = 'Анкета'

    name = models.TextField(
        verbose_name='Имя',
        null=True,
        blank=True,
    )

    text = models.TextField(
        verbose_name='Текст анкеты',
        null=True,
        blank=True,
    )

    city = models.TextField(
        verbose_name='Город',
        null=True,
        blank=True,
    )

    age = models.TextField(
        verbose_name='Возраст',
        null=True,
        blank=True,
    )

    profile_url = models.TextField(
        verbose_name='Ссылка',
        null=True,
        blank=True,
    )

    photo_url = models.TextField(
        verbose_name='Ссылка на фото',
        null=True,
        blank=True,
    )


class User(models.Model):
    class Meta:
        verbose_name = 'Пользователи'

    peer_id = models.IntegerField(
        verbose_name='peer id'
    )

    have_access = models.BooleanField(
        verbose_name='Есть доступ к БД',
        default=False
    )

    number_of_added = models.IntegerField(
        verbose_name='Количество добавленных анкет',
        default=0
    )

    profile_url_for = models.ForeignKey(
        Questionnaire,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    is_input_profile_url = models.BooleanField(
        verbose_name='Вводит ссылку на профиль',
        null=True,
        blank=True
    )