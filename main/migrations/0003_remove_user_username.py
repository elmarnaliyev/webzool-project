# Generated by Django 2.1.4 on 2018-12-09 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
