from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserInfo(models.Model):
    AIRCRAFTS_LST={
        'CDMT':'CDMT',
        'B74X':'B74X',
        'B737':'B737',
        'RJ10':'RJ10',
        'G650':'G650',
        'G550':'G550',
        'XLS+':'XLS+',
        'BE35':'BE35',
        'AW13':'AW13',

    }
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    aircraft=models.CharField(max_length=4,blank=True, choices=AIRCRAFTS_LST)
    
    def __str__(self):
        return f'{self.user.username}, {self.aircraft}'
        