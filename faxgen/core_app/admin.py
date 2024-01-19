from django.contrib import admin
from .models import OperationalFPL, Aircraft,Fax_elts

# Register your models here.
admin.site.register(OperationalFPL)
admin.site.register(Aircraft)
admin.site.register(Fax_elts)