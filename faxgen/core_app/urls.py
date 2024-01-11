from django.urls import path
from . import views

app_name='core_app'

urlpatterns = [
    path('upload/',views.fileUpload,name='upload')
]