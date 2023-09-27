from django.db import models


class profile(models.Model):
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
        ('othes', 'others'),

    )

    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    image = models.ImageField(upload_to='prof_pic/', default='def.png')
    phone = models.TextField(max_length=15)
    gender = models.CharField(choices=GENDER, max_length=8)
    deate_of_birth = models.CharField(max_length=15)

    def __str__(self):
        return self.name
