from django.shortcuts import render

from app1.models import tbl_shops

# Create your views here.
def index(request):
    return render(request, "index.html")
def add(request):
    return render(request,"add.html")
def add_shop(request):
    b=tbl_shops()
    b.name=request.POST.get('name')
    b.number=request.POST.get('number')
    b.state=request.POST.get('state')
    b.email=request.POST.get('email')
    b.save()
    return render(request, "index.html")