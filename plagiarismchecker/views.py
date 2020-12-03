from django.shortcuts import render
from django.http import HttpResponse
from plagiarismchecker.algorithm import main
from docx import *
from PyPDF2 import PdfFileReader


#import matplotlib.pyplot as plt
#from plagiarismchecker.algorithm import main

# Create your views here.
def home(request):
    return render(request, 'pc/index.html') 

def test(request):
    print("request is welcome test")
    print(request.POST['q'])  
    
    if request.POST['q']: 
        percent,link = main.findSimilarity(request.POST['q'])
    
    print("Output>>>>>>>>>>>>>>>>>>>>!!!!!!!!",percent,link)
    return render(request, 'pc/index.html',{'link': link, 'percent': percent})

def filetest(request):
    value = ''    
    print(request.FILES['docfile'])
    if str(request.FILES['docfile']).endswith(".txt"):
        value = str(request.FILES['docfile'].read())

    elif str(request.FILES['docfile']).endswith(".docx"):
        document = Document(request.FILES['docfile'])
        for para in document.paragraphs:
            value += para.text
    
    elif str(request.FILES['docfile']).endswith(".pdf"):
        pdfFileObj = open(str(request.FILES['docfile']), 'r') 
        print(pdfFileObj)

        
    percent,link = main.findSimilarity(value)
    print("Output>>>>>>>>>>>>>>>>>>>>!!!!!!!!",percent,link)
    return render(request, 'pc/index.html')
  

def fileCompare(request):
    return render(request, 'pc/doc_compare.html') 
    
