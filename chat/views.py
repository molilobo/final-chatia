from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required
def chat_home(request):
    return render(request,"chat/chat_home.html")

