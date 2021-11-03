from django.forms.widgets import RadioSelect
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from . models import ProductTable, SignUp
from website.forms import SignUpForm,LoginForm,UpdateForm,ChangePasswordForm,ProductForm
from django.contrib import messages
from django.contrib.auth import logout as logouts

# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=='POST':
        form=SignUpForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            name=form.cleaned_data['Name']
            designation=form.cleaned_data['Designation']
            email=form.cleaned_data['Email']
            pic=form.cleaned_data['Pic']
            password=form.cleaned_data['Password']
            cpass=form.cleaned_data['ConfirmPassword']
            phone=form.cleaned_data['Phone']
            user=SignUp.objects.filter(Email=email).exists()
            if user:
                messages.info(request,'email already existing')
                return redirect('register/')

            elif password!=cpass:
                messages.info(request,'password mismatch')
                return redirect('register/')
            else:
                table=SignUp(Name=name,Email=email,Password=password,Pic=pic,Designation=designation,Phone=phone)
                table.save()
                messages.success(request,'REGISTARION SUCCESSFULL')
                return redirect('/')

    else:
        form=SignUpForm
    return render(request,'register.html',{'form':form})   
def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            user=SignUp.objects.get(Email=email)
            if not user:
                messages.info(request,'user does not exist')
                return redirect('login/')
            elif password!=user.Password:
                messages.info(request,'password is incorrect')   
                return redirect('login/') 
            else:
                messages.success(request,'LOGIN SUCCESS')
                return redirect('/home/%s' % user.id)    
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})    

def home(request,id):
    user=SignUp.objects.get(id=id)
    return render(request,'home.html',{'user':user})  

def update(request,id):
    user=SignUp.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,request.FILES or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'UPDATE SUCCESSFULL')   
            return redirect('/home/%s' % user.id) 
    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'form':form,'user':user})

def changePass(request,id):
    user=SignUp.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            old=form.cleaned_data['Oldpassword']
            new=form.cleaned_data['Newpassword']
            cpass=form.cleaned_data['Confirmpassword']
            if old!=user.Password:
                messages.info(request,'Entered password is incorrect')
                return redirect('/changePass/%s' % user.id)
            elif new!=cpass:
                messages.info(request,'Password mismatch')
                return redirect('/changePass/%s' % user.id)
            else:
                user.Password=new
                user.save()
                messages.info(request,'SUCCESs')
                return redirect('/home/%s' % user.id)
    else:
        form=ChangePasswordForm()
    return render(request,'changepass.html',{'form':form,'user':user})    

def logout(request):
    logouts(request)
    messages.success(request,'SUCCESS')
    return redirect('/')

def product(request):
    pro=ProductTable.objects.all()
    return render(request,'gallery.html',{'pro':pro})
    
def productdetails(request,id):
    detail=ProductTable.objects.get(id=id)
    return render(request,'product.html',{'details':detail})
