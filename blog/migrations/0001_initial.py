# Generated by Django 3.0 on 2019-12-11 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComidaDeGato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sabor', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(max_length=20)),
                ('idade', models.IntegerField()),
                ('temperamento', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'gato',
                'verbose_name_plural': 'gatos',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='título')),
                ('text', models.CharField(max_length=200, verbose_name='texto')),
                ('author', models.CharField(max_length=60, verbose_name='autor')),
                ('created_date', models.DateField(verbose_name='data da criação')),
            ],
        ),
    ]
