# Created by Huzaifa
from django.http import HttpResponse 
from django.shortcuts import render # This helps render the HTML File on the Website

def index(request):
    return render(request,'index.html')
    



def analyze(request):
    djtext = request.POST.get('text','default') # to get a input from the webiste
    
    removepunc = request.POST.get('removepunc','false')
    fullcaps = request.POST.get('fullcaps','false') 
    newlineremover = request.POST.get('newlineremover','false') 
    charcounter = request.POST.get('charcounter','false') 
    espaceremover = request.POST.get('espaceremover','false')
    analyzed = ""
    purpose = ""
    
    
    #Punctuation Remover
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        purpose = " | Remove Punctuations"


    #UPPER CASE 
    if(fullcaps== "on"):
        if len(analyzed)!=0:
            analyzed = str.upper(analyzed)
        else:
            analyzed = str.upper(djtext)
        purpose += " | Changed to Upper Text"


    # New line remover
    if(newlineremover== "on"):
        c = ""
        if len(analyzed)!=0:
            djtext = analyzed
        for char in djtext:
            if char!="\n" and char!="\r":
                c += char
        analyzed = c
        purpose+= " | Removed New Lines"

    
    
    # Extra Space Remover
    if(espaceremover=="on"):
        txt = ""
        if len(analyzed)!=0:
            djtext = analyzed
        djtext = djtext.rstrip().lstrip() #causing error without this
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                txt += char
        analyzed =  txt
        purpose+= " | Removed Extra Spaces"

                
                
                
    # Character Counter
    if(charcounter== "on"):
        ccount = ""
        if len(analyzed)!=0:
            djtext = analyzed
        for char in djtext:
            if not (char==" "):
                ccount+= char
        analyzed += " The length of your Text is "+ str(len(ccount))
        purpose+= " | Character Count"  
   
   
    
    params = {'purpose':purpose,"analyzed_text":analyzed} 
    return render(request,'analyze.html',params)

    if removepunc== "false" and fullcaps=="false" and newlineremover=="false" and espaceremover=="false" and charcounter=="false":
        return HttpResponse("Error")    
    
