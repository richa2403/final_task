from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from Task_App.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from django.contrib.auth import login,logout
from Task_App.models import CustomUser
# Create your views here.

def loginpage(request):
    return render(request,"loginpage.html" ,{})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("loginpage")


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")

    else:
        user = EmailBackEnd.authenticate(request,username = request.POST.get("email"), password= request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type == "1":
                return HttpResponseRedirect('admin_home')
            elif user.user_type == "2":
                return HttpResponseRedirect('user_home')

        else:
            messages.error(request,"Invalid login Details")
            return HttpResponseRedirect("loginpage")

def createuser(request):
    return render(request,"createuser.html",{})

def createuser_save(request):
    if request.method!="POST":
        messages.error(request, "Invalid Method")
        return redirect('createuser')
    else:
        email = request.POST.get("email")
        username = request.POST.get("email")
        password = request.POST.get("password")
        # try:
        user = CustomUser.objects.create_user(username = username,password = password,user_type = 2, email=email)
        user.save()
        messages.success(request,"User Added Successfully")
        return HttpResponseRedirect("/createuser")

        # except:
        #     messages.error(request,"Failed to Add User")
        #     return HttpResponseRedirect("/createuser")