from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect
from django.urls import reverse


class LoginCheckMiddleWare(MiddlewareMixin):
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        print(modulename)
        user = request.user

        #Check whether the user is logged in or not
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "Task_App.adminviews":
                    pass
                elif modulename == "Task_App.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("admin_home")
            
            elif user.user_type == "2":
                if modulename == "Task_App.userviews":
                    pass
                elif modulename == "Task_App.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("user_home")

            else:
                return redirect("loginpage")

        else:
            if request.path == reverse("loginpage") or request.path == reverse("doLogin"):
                pass
            elif modulename == "Task_App.views":
                pass
            else:
                return redirect("loginpage")
