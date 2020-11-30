from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='plagiarism-check-mainpage'),
    path('compare', views.fileCompare,name='compare')
]
