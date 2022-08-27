# I have created this file  - Vishwajit
from string import punctuation
from django.http import HttpResponse
from django. shortcuts import render 

def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'index.html')

def analyze(request):
    dj=request.GET.get('text','default')
    
    removepunc = request.GET.get('removepunc','off')
    allcaps = request.GET.get('allcaps','off')
    new_line_remover = request.GET.get('new_line_remover','off')
    spaceremover = request.GET.get('spaceremover','off')

    
    if removepunc == "on":
            
        punctuations = '''!"#$%&'()*+-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        
        for char in dj:
            if char not in punctuations:
                analyzed = analyzed + char 
        params = {'purpose':'Remove Punctuations','analyzed_text': analyzed}
        dj= analyzed

    if(allcaps=="on"):
        analyzed = ""
        for char in dj:
            analyzed = analyzed + char.upper() 
        params = {'purpose':'Capitalize the Text','analyzed_text': analyzed}
        dj = analyzed
    
    if(new_line_remover=="on"):
        analyzed = ""
        for char in dj:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'New Line Remover','analyzed_text': analyzed}
        dj=analyzed

    if(spaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(dj):
            if not(dj[index] ==" " and dj[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'New Line Remover','analyzed_text': analyzed}

    if(removepunc != "on" and allcaps!= "on" and new_line_remover!= "on" and spaceremover!= "on"): 
        return HttpResponse('<h4>Error</h4>Please!! Select any operation and try again.')

    return render(request,'analyze.html',params)

def contact(request):
    return render(request,'contact.html')

