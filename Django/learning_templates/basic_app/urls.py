from django.urls import path, re_path
from django.conf.urls import  url
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative,name='relative'),
    path('other/',views.other,name='other')
]