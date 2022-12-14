# Generated by Django 4.1 on 2022-08-14 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='AboutUsImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('sub_text', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dejurniy', models.CharField(max_length=155)),
                ('buhgalteriya', models.CharField(max_length=155)),
                ('telegram', models.CharField(max_length=155)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Heros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Герои Топографы',
                'verbose_name_plural': 'Герои Топографы',
            },
        ),
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Requisites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=255)),
                ('RS', models.CharField(max_length=255)),
                ('INN', models.CharField(max_length=155)),
                ('OKOHX', models.CharField(max_length=255)),
                ('OKED', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Реквизиты',
                'verbose_name_plural': 'Реквизиты',
            },
        ),
        migrations.CreateModel(
            name='SendEmailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Отправленные емейлы',
                'verbose_name_plural': 'Отправленные емейлы',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('service_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('img', models.ManyToManyField(to='mainapi.aboutusimg')),
            ],
            options={
                'verbose_name': 'История',
                'verbose_name_plural': 'История',
            },
        ),
        migrations.CreateModel(
            name='AboutUsMore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255)),
                ('images', models.ManyToManyField(to='mainapi.images')),
            ],
            options={
                'verbose_name': 'О нас доп. информация',
                'verbose_name_plural': 'О нас доп. информация',
            },
        ),
    ]
