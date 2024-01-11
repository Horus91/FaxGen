from django.db import models

# Create your models here.
class OperationalFPL(models.Model):

    OFP_FORMAT={
    '0H':'0H',
    'OX':'OX',
    'ForeFlight':'ForeFlight',
    }

    ofp_format=models.CharField(max_length=10,choices=OFP_FORMAT)
    ofp=models.FileField(upload_to='ofps/',blank=True)

# class Aircraft(models.Model):
#     aircraft_type=models.CharField(max_length=10)
#     registration= models.CharField(max_length=5,unique=True)


# class Fax_elts(models.Model):
#     origin=models.CharField(max_length=4)
#     destination=models.CharField(max_length=4)
#     captain= models.CharField(max_length = 50)
#     aircraft=models.ForeignKey(Aircraft, on_delete=models.CASCADE)
#     departure=models.DateTimeField()
#     generated = models.DateTimeField(auto_add_now=False)