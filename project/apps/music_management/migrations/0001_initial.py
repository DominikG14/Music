# Generated by Django 5.0.4 on 2024-06-16 10:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yt_url', models.URLField()),
                ('name', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('alter_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yt_url', models.URLField()),
                ('title', models.CharField(max_length=255)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('file_size', models.IntegerField(blank=True, null=True)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('alter_date', models.DateField(default=django.utils.timezone.now)),
                ('artists', models.ManyToManyField(to='music_management.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('alter_date', models.DateField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255)),
                ('songs', models.ManyToManyField(to='music_management.song')),
            ],
        ),
    ]
