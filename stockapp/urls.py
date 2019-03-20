from django.urls import path, include
from . import views

app_name = 'stock_app'

urlpatterns = [

    path('', views.Home.as_view(), name='home'),
    path('upload/', views.UploadData.as_view(), name='upload'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('settings/', views.SettingsList.as_view(), name='settings'),
    path(r'new_settings', views.ApiSettingsCreate.as_view(), name='new_settings'),


]