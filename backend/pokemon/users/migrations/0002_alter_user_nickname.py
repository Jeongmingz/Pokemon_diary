# Generated by Django 3.2 on 2023-09-03 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.TextField(db_column='user_nickname', verbose_name='user_nickname'),
        ),
    ]