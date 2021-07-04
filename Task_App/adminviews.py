import os
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
import random


def admin_home(request):
    return render(request,"admin_dasboard.html",{})

