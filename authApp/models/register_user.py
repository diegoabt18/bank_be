from django.db import models

class Register_user(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    nickname = models.CharField(max_length = 15, unique=True)
    password = models.CharField(max_length = 256)
    email = models.EmailField(max_length = 100)
    adress = models.CharField(max_length = 100)
    cellphone = models.CharField(max_length = 15)
    