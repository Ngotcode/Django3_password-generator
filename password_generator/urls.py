"""password_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin       #Teri: ot using this yet, that import admin studd
from django.urls import path

from generator import views          #Teri: add this line
urlpatterns = [
   # path('admin/', admin.site.urls),          #also can delete this for now
   #path('', views.home),          #teri: add this line
   path('', views.home, name='home'), 
   #path('eggs', views.eggs),       #try adding this line to show in webpage called eggs
   #path('password/', views.password),     #this takes to a another page with password display, #good to add ending /
  
   path('password/', views.password, name='password'), 
   #path('generatedpassword/', views.password, name='password'), #this will have "generalpassword on the url line"

   path('about/', views.about, name='about'),        #create an "about" page

]                               

