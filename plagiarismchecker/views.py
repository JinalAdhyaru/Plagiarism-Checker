from django.shortcuts import render
from django.http import HttpResponse
from plagiarismchecker.algorithm import main
#from plagiarismchecker.algorithm import main

# Create your views here.
def home(request):
    return render(request, 'pc/index.html') 

def test(request):
    print("request is welcome test")
    print(request.POST['q'])
    
    if request.POST['q'] != '' : 
        print("hurray its q")
        result = main.findSimilarity(request.POST['q'])
   
    print("Output>>>>>>>>>>>>>>>>>>>>!!!!!!!!", result)
    return render(request, 'pc/index.html',{'result': result })

def filetest(request):
    value = ''    
    print(request.FILES['docfile'])
    if "txt" in str(request.FILES['docfile']):
        value = str(request.FILES['docfile'].read())
    
    print(value)
    result = main.findSimilarity(value)
    return render(request, 'pc/index.html',{'result' : result})
  

def fileCompare(request):
    return render(request, 'pc/doc_compare.html') 
    
