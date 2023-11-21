from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from appstore.forms import LoginForms, SignupForms
from appstore.models import Product

# Create your views here.
def home(request):
    # product= Product.objects.all()
    maleitem=Product.objects.filter(type__name="Male")[0:4]
    femaleitem=Product.objects.filter(type__name="Female")[0:4]
    child=Product.objects.filter(type__name="Chaild")[0:4]
    toy=Product.objects.filter(type__name="Toy")[0:4]
    
    contex={
        'productM':maleitem,
        'productF':femaleitem,
        'productC':child,
        'productT':toy,
    }
    
    return render(request,"home.html",contex)

def mens(request):
    maleitem=Product.objects.filter(type__name="Male")
    
    return render(request,'mens.html',{"maleitem":maleitem})

def females(request):
    females=Product.objects.filter(type__name="Female")
    return render(request,'femals.html',{'females':females})

def toy(request):
    toys=Product.objects.filter(type__name="Toy")
    return render(request,'toy.html',{'toys':toys})

def chaild(request):
    chailds=Product.objects.filter(type__name="Chaild")
    return render(request,'chaild.html',{'chailds': chailds})

def details(request,id):
    product=Product.objects.get(id=id)
    return render(request,'details.html',{'product':product})




def signupPage(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form=SignupForms(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Signup successfully")
                return redirect("login")
            else:
                messages.error(request,'signup fail ')
        else:    
            form=SignupForms()
        return render(request,'signup.html',{"form":form})

    else:
        return redirect('home')
    
def loginPage(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            form=LoginForms(request=request, data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user:
                    login(request,user)
                    messages.success(request,"login succefully")
                    return redirect('home')
            else:
                messages.error(request,'login fail try agein')
                return redirect('login')
        else:        
            form=LoginForms()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('home')
    
def logoutPage(request):
    logout(request)
    return redirect("login")   

