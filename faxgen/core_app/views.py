from django.shortcuts import render
from .forms import OperationalFPLForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from static.pdfextract import Fax_elts, Fax_docx


# Create your views here.
@login_required
def fileUpload(request):
    if request.method == 'POST':
        form = OperationalFPLForm(request.POST)
        if form.is_valid():
            ofp_final=form.save()
            if 'ofp' in request.FILES:
                print('FILE INBOUND')
                ofp_final.ofp=request.FILES['ofp']
            ofp_final.save()
            return HttpResponseRedirect(reverse('login_app:login'))
        else:
            print(form.errors)
    else:
        form=OperationalFPLForm()
        return render(request,'core_app/upload.html',{'form':form})
