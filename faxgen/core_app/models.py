from time import strftime
from django.db import models
from django.utils import timezone




# Create your models here.
class OperationalFPL(models.Model):

    OFP_FORMAT={
    '0H':'0H',
    'OX':'OX',
    'ForeFlight':'ForeFlight',
    }
    ofp_format=models.CharField(max_length=10,choices=OFP_FORMAT)
    ofp=models.FileField(upload_to='ofps/',blank=True,verbose_name="Operation FPL:")

    def __str__(self):
        return f"{self.ofp}"

class Aircraft(models.Model):
    aircraft_type=models.CharField(max_length=10)
    registration= models.CharField(max_length=5,unique=True)

    def __str__(self):
        return f"{self.aircraft_type}: {self.registration}"


class Fax_elts(models.Model):
    captain= models.CharField(max_length = 50)
    aircraft=models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    fir_countries = models.TextField(verbose_name='Countries:')
    fir_points = models.TextField(verbose_name='FIR points:')
    generated_file=models.OneToOneField(OperationalFPL,on_delete=models.CASCADE)
    generated = models.DateTimeField(auto_now_add=False,default= timezone.now)

    def __str__(self):
        return f"{self.generated_file} | {self.generated}"