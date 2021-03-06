# Generated by Django 3.1.1 on 2020-09-22 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Область поиска')),
            ],
            options={
                'verbose_name': 'Область поиска',
                'verbose_name_plural': 'Области поиска',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='ID Пользователя')),
            ],
            options={
                'verbose_name': 'Пользователь бота',
                'verbose_name_plural': 'Пользователи бота',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.TextField(verbose_name='запрос')),
                ('result', models.TextField(verbose_name='результат')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='дата запроса')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ID', to='bot_geokoder.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Результат поиска',
                'verbose_name_plural': 'Результаты поиска',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='result',
            field=models.ManyToManyField(to='bot_geokoder.Result', verbose_name='Результат поиска'),
        ),
    ]
