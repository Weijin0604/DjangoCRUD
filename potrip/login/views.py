from django.shortcuts import render
from django.http.response import HttpResponse
from .models import User
# Create your views here.
def index(request):
    user1 = User.objects.all()
    user2 = User.objects.get(id=1)
    user3 = User.objects.filter(password = "1234")
    #SELECT * FROM User
    return render(request, "login/index.html",{"User":user1})