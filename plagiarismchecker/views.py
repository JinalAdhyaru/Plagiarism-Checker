from django.shortcuts import render
from django.http import HttpResponse
from plagiarismchecker.algorithm import main
#from plagiarismchecker.algorithm import main

# Create your views here.
def home(request):
    return render(request, 'pc/index.html') 

#text websearch
def test(request):
    print("request is welcome test")
    print(request.POST['q'])
    
    if request.POST['q'] != '' : 
        print("hurray its q")
        result = main.findSimilarity(request.POST['q'])
   
    print("Output>>>>>>>>>>>>>>>>>>>>!!!!!!!!", result)
    return render(request, 'pc/index.html',{'result': result })

#single file upload web search
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

#two text compare
def twofiletest1(request):
    print("Submiited text for 1st and 2nd")
    print(request.POST['q1'])
    print(request.POST['q2'])
    return render(request, 'pc/doc_compare.html')    
    
# def twofiletest2(request):
#     print("Submiited text for 2nd")
#     return render(request, 'pc/doc_compare.html')

#two file compare
def twofilecompare1(request):
    print("Submiited file for 1st")
    return render(request, 'pc/doc_compare.html')

# def twofilecompare2(request):
#     print("Submiited text for 2nd")
#     return render(request, 'pc/doc_compare.html')