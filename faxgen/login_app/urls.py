from django.urls import path
from login_app import views

app_name='login_app'

urlpatterns = [
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('photo/',views.photo,name='photo'),
]