from django.urls import path
from . import views

app_name='core_app'

urlpatterns = [
    path('upload/',views.fileUpload,name='upload'),
    path('history/',views.history_view,name='history'),
    path('<int:id>/',views.download_view,name="download")

]