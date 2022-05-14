from django.shortcuts import render
from register.models import Registrations


# Create your views here.
def index(request):
    reg=Registrations.objects
    bcount=reg.filter(Contest="Basic programming").count()
    acount=reg.filter(Contest="Advance programming").count()
    gcount=reg.filter(Contest="Online gaming").count()
    pcount=reg.filter(Contest="Project making").count()
    data = {'bcount':bcount,'acount':acount,'gcount':gcount,'pcount':pcount}
    return render(request,"home/index.html",data)
    # return render(request,"home/index.html")