from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='plagiarism-check-mainpage'),
    path('compare/', views.fileCompare,name='compare'), 
    path('test/', views.test,name='Test'),
    path('filetest/', views.filetest,name='filetest'),
     path('twofiletest1/', views.twofiletest1,name= 'twofiletest1'),
    #path('twofiletest2/', views.twofiletest2,name= 'twofiletest2'),
    path('twofilecompare1/', views.twofilecompare1,name= 'twofilecompare1'),
    #path('twofilecompare2/', views.twofilecompare2,name= 'twofilecompare2')
]
