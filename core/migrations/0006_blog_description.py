# Generated by Django 3.1.5 on 2021-03-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_blog_hello'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default='Hello, world!', max_length=200),
            preserve_default=False,
        ),
    ]
