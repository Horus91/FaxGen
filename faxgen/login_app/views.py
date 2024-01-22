from django.shortcuts import render
from login_app.forms import UserForm,UserInfoForm


# LOGIN/OUT IMPORTS
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

# def register_view(request):

#     if request.method == 'POST':
#         uform=UserForm(data=request.POST)
#         pform=UserInfoForm(data=request.POST)
#         if uform.is_valid() and pform.is_valid():
#             user=uform.save()
#             user.set_password(user.password) #HASHING PASSWORD
#             # user.set_password(make_password(user.password2))
#             user.save()

#             profil=pform.save(commit=False)
#             profil.user=user

#             profil.save()

#             return HttpResponseRedirect(reverse('login'))
#             # return HttpResponse('<h1>IN</h1>')

#         else:
#              print(UserForm.errors,UserInfoForm.errors)

#     else:
#         uform=UserForm()
#         pform=UserInfoForm()
#     return render(request,'login_app/register.html',{'uform':uform,
#                                                      'pform':pform})

def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        myuser = authenticate(request, username = username , password = password )
        if myuser:
            if myuser.is_active:
                login(request,myuser)
                return HttpResponseRedirect(reverse('login_app:login'))
            else:
                return HttpResponse('<h1>NOT ACTIVE</h1>')
        else:
            return HttpResponseRedirect(reverse('login_app:login'))

    else:
        return render(request,'login_app/login.html',{})

@login_required()
def photo(request):
    return render(request,'photo.html')

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_app:login'))


