from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Trainee
from .forms import TraineeForm



# Create your views here.

def show(request):
    trainees = Trainee.objects.all()
    return render(request, "show.html", {'trainees':trainees})


def deleteRecord(request, id):
    trainee = Trainee.objects.get(TraineeID=id)
    trainee.delete()
    return redirect("/")


def emailSend(request):
    subject = "Due's Payment Notification"
    msg = "Please pay your due amount within seven(07) day's from today."
    to = []
    for trn in Trainee.objects.all():
        if trn.DueAmount>0:
            to.append(trn.EmailAddress)
        else:
            pass
    res = send_mail(subject, msg, EMAIL_HOST_USER, to, fail_silently=False)
    if res == 1:
        msg = "Your Email Sent Successfully!!!"
    else:
        msg = "Your Email Could Not Sent!!!"
    return HttpResponse(msg)


def recordSave(request):
    if request.method == "POST":
        form = TraineeForm(request.POST)
        try:
            form.save()
            return redirect("/")
        except:
            pass
    else:
        form = TraineeForm()

    return render(request, 'index.html', {'form': form})


def editRecord(request, id):
    trainee = Trainee.objects.get(TraineeID=id)
    return render(request, 'edit.html', {'trainee':trainee})


def updateRecord(request, id):
    trainee = Trainee.objects.get(TraineeID=id)
    form = TraineeForm(request.POST, instance=trainee)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {'trainee': trainee})



