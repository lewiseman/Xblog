# Generated by Django 3.1.3 on 2020-12-22 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('authour', models.CharField(max_length=100)),
                ('authour_image', models.ImageField(upload_to='AuthorImages')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('content_image', models.ImageField(upload_to='ContentImage')),
                ('slug', models.SlugField(default=None)),
            ],
            options={
                'verbose_name': 'Story',
                'verbose_name_plural': 'Stories',
            },
        ),
    ]
