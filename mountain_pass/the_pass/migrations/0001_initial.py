# Generated by Django 5.0.3 on 2024-03-24 13:01

import django.core.validators
import django.db.models.deletion
import the_pass.services
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('height', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Координаты',
                'verbose_name_plural': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(choices=[(' ', ' '), ('1A', '1A'), ('2A', '2A'), ('3A', '3A'), ('4A', '4A')], default=' ', max_length=2)),
                ('summer', models.CharField(choices=[(' ', ' '), ('1A', '1A'), ('2A', '2A'), ('3A', '3A'), ('4A', '4A')], default=' ', max_length=2)),
                ('autumn', models.CharField(choices=[(' ', ' '), ('1A', '1A'), ('2A', '2A'), ('3A', '3A'), ('4A', '4A')], default=' ', max_length=2)),
                ('spring', models.CharField(choices=[(' ', ' '), ('1A', '1A'), ('2A', '2A'), ('3A', '3A'), ('4A', '4A')], default=' ', max_length=2)),
            ],
            options={
                'verbose_name': 'Уровень сложности',
                'verbose_name_plural': 'Уровни сложности',
            },
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fam', models.CharField(max_length=50)),
                ('otc', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть введён в следующем формате: '+78005553535' 11 цифр.", regex='^\\+\\d{11}$')])),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('other_titles', models.CharField(max_length=255)),
                ('connect', models.TextField()),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'новый'), ('pending', 'модератор взял в работу'), ('accepted', 'модерация прошла успешно'), ('rejected', 'модерация прошла, информация не принята')], default='new', max_length=20)),
                ('coords', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='the_pass.coord')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='the_pass.level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='the_pass.myuser')),
            ],
            options={
                'verbose_name': 'Перевал',
                'verbose_name_plural': 'Перевалы',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('data', models.ImageField(null=True, upload_to=the_pass.services.get_path_upload_photo)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('pereval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='the_pass.pereval')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
