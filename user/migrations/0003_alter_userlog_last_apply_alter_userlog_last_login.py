# Generated by Django 4.0.4 on 2022-06-17 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='last_Apply',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userlog',
            name='last_login',
            field=models.DateField(auto_now=True),
        ),
    ]
