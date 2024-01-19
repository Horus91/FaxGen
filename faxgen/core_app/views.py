import os
from django.shortcuts import render
from .forms import OperationalFPLForm,Fax_eltsForm
from .models import OperationalFPL
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from static.pdfextract import OFPS_DIR, Fax_elts, Fax_docx



# Create your views here.
@login_required
def fileUpload(request):
    if request.method == 'POST':
        com_form=Fax_eltsForm(request.POST)
        form = OperationalFPLForm(request.POST,request.FILES)
        if com_form.is_valid() and form.is_valid():
            ofp_elts = com_form.save(commit=False)
            if 'ofp' in request.FILES:
                print('FILE INBOUND')
                the_fax=Fax_docx(ofp_elts.fir_countries,ofp_elts.fir_points,ofp_elts.aircraft.aircraft_type,ofp_elts.captain,Fax_elts(request.FILES['ofp']))
                the_fax.generate_fax()
                path=OFPS_DIR.joinpath(f'{the_fax.general_infos[0]}-{the_fax.captain}-{the_fax.general_infos[2][:4]}-{the_fax.general_infos[3][:4]}.docx')
                with path.open(mode='rb') as f:
                    fax = OperationalFPL.objects.create()
                    fax.ofp.save(f'{the_fax.general_infos[0]}-{the_fax.captain}-{the_fax.general_infos[2][:4]}-{the_fax.general_infos[3][:4]}.docx',f,save=True)
                    ofp_elts.generated_file=fax
                    ofp_elts.save()
                    f.close()
                    os.remove(path)
                    return HttpResponseRedirect(reverse('login_app:login'))
        else:
            print(form.errors)
    else:
        com_form=Fax_eltsForm()
        form=OperationalFPLForm()
        return render(request,'core_app/upload.html',{'com_form':com_form 
                                                      ,'form':form})
