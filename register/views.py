
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from register.models import Registrations
from django.contrib import messages

# Create your views here.


def formbasic(request):
    return render(request, 'register/registerbase.html', {'event': 'Basic programming'})


def formadvance(request):
    return render(request, 'register/registerbase.html', {'event': 'Advance programming'})


def formgaming(request):
    return render(request, 'register/registerbase.html', {'event': 'Online gaming'})


def formproject(request):
    return render(request, 'register/registerbase.html', {'event': 'Project making'})


def submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        roll = request.POST["rollnumber"]
        event = request.POST['event']
        dbroll = Registrations.objects.filter(Roll=int(roll)).filter(Contest=event)
        d = Registrations.objects.filter(Contest =event).count()
        dic={'Project making':25,'Online gaming':90,'Advance programming':50,'Basic programming':100}
        # print(d,dic[event],event)
        if d >= dic[event]:
            print(d >= dic[event])
            messages.success(request, "Registrations are completed!")
            return redirect("/")
        # print(event)
        if(len(roll) != 13) or (int(roll[3:6]) not in (783, 231)) or (int(roll[0]) not in (1, 2, 9)) or (int(roll[1])not in (0, 1)):
            messages.success(request, "Wrong Roll Number!")
            return redirect("/")
        if (dbroll.exists()):
            messages.success(request, "User already Exists!")
            return redirect("/")
        branch = request.POST['branch']
        year = request.POST['year']
        sec = request.POST['sec']
        email = request.POST['email']
        # print(name, branch, year, event, sec, email)
        # if(event == 'Basic programming' and )
        details = Registrations(Name=name, Year=year, Branch=branch, Section=sec,Email=email, Contact_No=phone, Contest=event, Roll=int(roll))
        details.save()
        messages.success(request, 'Registered Succesfully!')
    return HttpResponseRedirect('/')
