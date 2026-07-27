#hello this 
from os import remove
from urllib import request

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    info = {
        'name': 'Sargam','place': 'Behror'}
    return render(request, 'index.html',info)
    # return HttpResponse("Hello, world.<h1>Sargam</h1>here. <a href='https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7'>youtube</a>")

# def about(request):
#     return HttpResponse("This is the about page.")
def navigation(request):
    s = """<h2>Navigation</h2>
    <a href="https://www.google.com/">Google</a><br>
    <a href="https://www.youtube.com/watch?v=lcpqpxVowU0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=12">Youtube</a><br>"""
    return HttpResponse(s)
    
def analyze(request):
    p=request.GET.get('text', 'default')
   
    print(request.GET.get('removepunc', 'off'))
    print(p)
    print(request.GET.get('fullcaps', 'off'))
   
    if (request.GET.get('removepunc', 'off') == 'on'):

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in p:

            if char not in punctuations:
                analyzed = analyzed + char
        
        remove = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        p=analyzed
        # return render(request, 'analyze.html', remove)
    
    if (request.GET.get('fullcaps', 'off') == 'on'):
        analyzed=""
        for char in p:
            analyzed = analyzed + char.upper()
        remove = {'purpose': 'Convert to Uppercase', 'analyzed_text': analyzed}
        p=analyzed
        # return render(request, 'analyze.html', fullcaps)
    
    if (request.GET.get('newlineremover', 'off') == 'on'):
        analyzed = p.replace('\r\n', ' ')
        remove = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        p = analyzed  
        # return render(request, 'analyze.html', newlineremover)
    
    if (request.GET.get('extraspaceremover', 'off') == 'on'):
        analyzed=""
        for index, char in enumerate(p):
            if not(p[index] == " " and index+1 < len(p) and p[index+1]==" "):
                analyzed = analyzed + char
        remove = {'purpose': 'Remove extra space', 'analyzed_text': analyzed}
        p=analyzed
        # return render(request, 'analyze.html', extraspaceremover)
    
    if (request.GET.get('charcount', 'off') == 'on'):
        analyzed=""
        count=0
        for char in p:
            if char != " ":
                count+=1
        remove = {'purpose': 'Count characters', 'analyzed_text': count}
        p=analyzed
        # return render(request, 'analyze.html', charcount)

    if (request.GET.get('removepunc', 'off') != 'on' and request.GET.get('fullcaps', 'off') != 'on' and request.GET.get('newlineremover', 'off') != 'on' and request.GET.get('extraspaceremover', 'off') != 'on' and request.GET.get('charcount', 'off') != 'on'):
        return HttpResponse("Please select any operation and try again.<a href=/>back</a>")
    
    return render(request, 'analyze.html', remove) 

 
          
    


# def capitalizefirst(request):
#     return HttpResponse("This is the capitalize first letter page.")

# def newlineremove(request):
#     return HttpResponse("This is the new line remove page.")

# def spaceremove(request):
#     return HttpResponse("This is the space remove page.<a href=/>back</a>")

# def charcount(request):
#     return HttpResponse("This is the character count page.<a href=/>back</a>")