# Generated by Django 4.0.4 on 2022-06-17 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.CharField(max_length=20, verbose_name='유저 타입')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, verbose_name='이름')),
                ('password', models.CharField(max_length=128, verbose_name='비밀번호')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='이메일 주소')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('usertype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type', to='user.usertype')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
