# Generated by Django 2.1.4 on 2018-12-09 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('website_url', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('business_type', models.CharField(max_length=200)),
                ('owner_name', models.CharField(max_length=200)),
                ('domain', models.CharField(max_length=200)),
                ('website_type', models.CharField(max_length=200)),
            ],
        ),
    ]
