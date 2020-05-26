from django.shortcuts import render

from django.http import HttpResponse         #teri: create new line here
import random

# Create your views here.
#Teri: create new function here
def home(request):
    #return render(request, 'generator-app/home.html', {'password':'thisisapassword'})

    return render(request, 'generator-app/home.html')

   # return render(request, 'generator-app/home.html')
    #return HttpResponse("Hello there friend!")      
    #webpage localhost:8000 house now say Hello there friend

#def eggs(request):
   # return HttpResponse('Eggs are so tasty')

    #webpage localhost:8000/eggs house now says Egss are so tasty

#def eggs(request):
 #   return HttpResponse('<h1>Eggs are so tasty</h1>')     #this is not a good way to return html code inside a string


#def password(request):
  #   return render(request, 'generator-app/password.html')

def password(request):

    #thepassword = 'testing'
    characters =list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXWZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*(()"'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))


    #length = 10     #arbitary length works with password length of 10
    length = int(request.GET.get('length', 12))       #use 12 as the default length
    
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator-app/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator-app/about.html')