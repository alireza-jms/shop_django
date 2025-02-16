#from django.http import HttpResponse
from django.template import loader


from django.shortcuts import render, redirect
from .models import Product , Category

from django.contrib.auth import authenticate,login,logout #برای احرازهویت
from django.contrib import messages
from django.contrib.auth.models import User #برای ثبت نام 
from django.contrib.auth.forms import UserCreationForm #برای ثبت نام 
from django import forms
from .forms import signupforms



def home(request):
     products = Product.objects.all()
     #return HttpResponse (products)
     return render(request, 'index.html',{'products':products})

def about(request):
     return render(request, 'about.html')

def login_user(request):
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username , password=password)
        if user is not None:
             login(request,user) 
             messages.success(request,"با موفقیت وارد شدید") 
             return redirect("home") 
        else:
            messages.success(request," دوباره تلاش کنید  رمز اشتباه بود ") 
            return redirect("login") 
    else: 
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ("باموفقیت خارج شدید "))
    return redirect ("home")

def signup_user(request):
    form=signupforms()
    if request.method =="POST":
        form=signupforms(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data['username']
            password1 =form.cleaned_data['password1']
            user = authenticate(request, username=username , password=password1)
            login(request,user) 
            messages.success(request," اکانت شما ساخته شد ") 
            return redirect("home") 
        else:
            messages.success(request,('ثبت نام انجام نشد دوباره ثبت نام کنید'))  
            return redirect("signup") 
    else :
          return render (request, 'signup.html',{'form':form})

def product(request,pk):                                    #   صفحه نشان دادن یک محصول درصحفه جدا   
     product = Product.objects.get(id=pk)
     
     return render(request, 'product.html',{'product':product})    


## def category(request,cat): 
  
 #   cat=  cat.replace("-","")  
 #   try:
#     category = Category.objects.get(name=cat)
#     product = Product.objects.get(id=pk)
#     return render(request, 'category.html',{'products':product,"category":category})    
#    except:     
 #      messages.success(request,('دسته بندی وجود ندارد'))  
#       return redirect("home")    ##
 
 
#def category(request, cat):
    # فیلتر کردن محصولات بر اساس نام دسته‌بندی
   # products = Product.objects.filter(Category__name=category_name)
  #  return render(request, 'category.html', {'products': products})