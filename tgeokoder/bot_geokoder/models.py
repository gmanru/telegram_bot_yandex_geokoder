from django.db import models

# Create your models here.
class Profile(models.Model):
    user_id = models.PositiveIntegerField(
        verbose_name='ID Пользователя',
        unique=True,
        primary_key=True
    )

    result = models.ManyToManyField(
        'Result',
        verbose_name='Результат поиска',
    )

    def __str__(self):
        return f'{self.user_id}'

    '''def __str__(self):
        return f'#{self.external_id} {self.name}'''

    class Meta:
        verbose_name = 'Пользователь бота'
        verbose_name_plural = 'Пользователи бота'

class Filter(models.Model): #область поиска
    '''profile = models.ForeignKey(
        to='bot_geokoder.Profile',
        verbose_name='Профиль',
        on_delete=models.PROTECT,
    )'''
    
    text = models.TextField(
        verbose_name='Область поиска',
    )
    '''created_at = models.DateTimeField(
        verbose_name='Время получения',
        auto_now_add=True,
    )

    def __str__(self):
        return f'Сообщение {self.pk} от {self.profile}'''

    class Meta:
        verbose_name = 'Область поиска'
        verbose_name_plural = 'Области поиска'

    def __str__(self):
        return self.text


class Result(models.Model):
    uid = models.ForeignKey('Profile',
    verbose_name='Профиль',on_delete=models.CASCADE,
    related_name='ID',)
    
    request = models.TextField(
        verbose_name='запрос',
    )

    result = models.TextField(
        verbose_name='результат',
    )

    created_at = models.DateField(
        verbose_name='дата запроса',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Результат поиска'
        verbose_name_plural = 'Результаты поиска'

    def __str__(self):
        return  f'{self.request} -> {self.result} ({self.created_at})'

