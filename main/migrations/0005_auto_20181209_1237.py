# Generated by Django 2.1.4 on 2018-12-09 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='full_name',
        ),
    ]
