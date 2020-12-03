from django.shortcuts import render
from django.http import HttpResponse
from plagiarismchecker.algorithm import main
from plagiarismchecker.algorithm import fileSimilarity
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

#two text compare
def twofiletest1(request):
    print("Submiited text for 1st and 2nd")
    print(request.POST['q1'])
    print(request.POST['q2'])

    if request.POST['q1'] != '' and request.POST['q2'] != '': 
        print("Got both the texts")
        result = fileSimilarity.findFileSimilarity(request.POST['q1'],request.POST['q2'])
        
    print("Output>>>>>>>>>>>>>>>>>>>>!!!!!!!!",result)
    return render(request, 'pc/doc_compare.html',{'result': result})
    
# def twofiletest2(request):
#     print("Submiited text for 2nd")
#     return render(request, 'pc/doc_compare.html')

#two file compare
def twofilecompare1(request):
    value1 = ''
    value2 = ''
    print("Submiited files for 1st and 2nd")
    print(request.FILES['docfile1'])
    print(request.FILES['docfile2'])
    if "txt" in str(request.FILES['docfile1']) and "txt" in str(request.FILES['docfile2']):
        value1 = str(request.FILES['docfile1'].read())
        value2 = str(request.FILES['docfile2'].read())
    result = fileSimilarity.findFileSimilarity(value1,value2)
    print(value1)
    print(value2)
    print("Output>>>>>>>>>>>>>>>>>>>>!!!!!!!!",result)
    return render(request, 'pc/doc_compare.html',{'result': result})

# def twofilecompare2(request):
#     print("Submiited text for 2nd")
#     return render(request, 'pc/doc_compare.html')    
    
