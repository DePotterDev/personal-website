# Generated by Django 3.1.5 on 2021-03-05 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_blog_hello'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='hello',
        ),
    ]
