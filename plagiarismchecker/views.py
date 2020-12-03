from django.shortcuts import render
from django.http import HttpResponse
from plagiarismchecker.algorithm import main
#import matplotlib.pyplot as plt
#from plagiarismchecker.algorithm import main

# Create your views here.
def home(request):
    return render(request, 'pc/index.html') 

def test(request):
    print("request is welcome test")
    print(request.POST['q'])  
    
    '''value = ''
    #if !request.POST['q'] :
    if "txt" in str(request.FILES['docfile']):
        value = str(request.FILES['docfile'].read())
    '''
    if request.POST['q'] != '' : 
        print("hurray its q")
        percent,link = main.findSimilarity(request.POST['q'])
        percent = round(percent,2)
    print("Output>>>>>>>>>>>>>>>>>>>>!!!!!!!!",percent,link)
    return render(request, 'pc/index.html',{'link': link, 'percent': percent})

def filetest(request):
    value = ''    
    print(request.FILES['docfile'])
    if "txt" in str(request.FILES['docfile']):
        value = str(request.FILES['docfile'].read())
    
    print(value)
    return render(request, 'pc/index.html')
  

def fileCompare(request):
    return render(request, 'pc/doc_compare.html') 
    
