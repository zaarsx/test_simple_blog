# Generated by Django 3.0.5 on 2020-05-02 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('image', models.ImageField(upload_to='blog/blogpost', verbose_name='image')),
                ('text', models.TextField(verbose_name='text')),
                ('published', models.DateTimeField(blank=True, null=True, verbose_name='piblished at')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'ordering': ['-published'],
            },
        ),
    ]