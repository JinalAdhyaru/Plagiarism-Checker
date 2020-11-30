from django.shortcuts import render
from django.http import HttpResponse
from plagiarismchecker.algorithm import main
#from plagiarismchecker.algorithm import main

# Create your views here.
def home(request):
    return render(request, 'pc/index.html') 

def test(request):
    print(request.GET['q'])
    result = main.findSimilarity(request.GET['q'])
    print("Output>>>>>>>>>>>>>>>>>>>>!!!!!!!!", result)
    return render(request, 'pc/index.html',{'result': result})

def filetest(request):
    print(request.FILES['docfile'])
    return render(request, 'pc/index.html')
    

def fileCompare(request):
    return render(request, 'pc/doc_compare.html') 
    