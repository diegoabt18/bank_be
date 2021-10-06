# Generated by Django 3.2.8 on 2021-10-06 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register_user',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=100)),
                ('adress', models.CharField(max_length=100)),
                ('cellphone', models.CharField(max_length=15)),
            ],
        ),
    ]