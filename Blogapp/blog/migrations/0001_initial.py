# Generated by Django 5.0.7 on 2024-07-30 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='blogs')),
                ('story', models.CharField(max_length=1000)),
                ('published_date', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('categories', models.ManyToManyField(blank=True, to='blog.category')),
            ],
        ),
    ]
