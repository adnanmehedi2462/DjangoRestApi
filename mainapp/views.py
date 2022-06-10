
from django.shortcuts import render,get_object_or_404,HttpResponse,Http404,redirect,HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Myplanserializers
from rest_framework import viewsets
from .models import *
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView

@api_view(['GET', 'POST'])



def firstapi(request):
    if request.method == "POST":
        username=request.data['username']
        email=request.data['email']
        
        print(username,email)
        return Response({"username":username,"email":email})
    context={
        "username":"Al-Adnan-Mehedi",
        "email":"tasnimMostofarafa@gmail"
    },{
        "username":"nehal",
        "email":"rafa@gmail.com"        
    }
    
    return Response (context)
    



def Home(request):
    return render(request,"index.html")




from django.contrib.auth.models import User

@api_view(['POST','GET'])

def RegistationApi(request):
    if request.method == "POST":
        username=request.data['username']
        email=request.data['email']
        first_name=request.data['first_name']
        last_name=request.data['last_name']
        password1=request.data['password1']
        password2=request.data['password2']
        if User.objects.filter(username=username).exists():
            return Response({"Error": "username already Exist...!!!!"})
        if password1!=password2:
            return Response({"Error" : "Passwords Not Same !!!! "})
        
        if User.objects.filter(email=email).exists():
            return Response({"Error": "Email already Exist...!!!!"})  
        
        user=User() 
        
        user.username=username
        user.email=email    
        user.first_name=first_name 
        user.last_name=last_name
        user.set_password(raw_password=password1)
        user.is_active=True
        user.is_staff=True
        user.save()
        return Response({"Success":"User Resister Successfully!!"})
          
    


# new todo app////////////////////////////////////////////////

class planlist (ListAPIView):
    queryset=plan.objects.all()
    serializer_class=Myplanserializers
    
    
    
class plancreate (CreateAPIView):
    queryset=plan.objects.all()
    serializer_class=Myplanserializers
    
    
    
class plandelete (DestroyAPIView):
    queryset=plan.objects.all()
    serializer_class=Myplanserializers