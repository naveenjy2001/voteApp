from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import voteoption,receive,received_feedback,updates

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            cand = voteoption.objects.all()
            return render(request,"vote.html", {'candidates': cand})
        else:
            messages.info(request,'Invalid Email or Password')
            return render(request,'index.html')
    else:

        return render(request,'index.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def update(request):
    news = updates.objects.all()
    return render(request,'updates.html', {'upd': news})

def contact(request):
    return render(request,'contact.html')

def feedback(request):
    return render(request,'feedback.html')

def feedbacksubmit(request):
    feedback = request.POST['feedback']
    data = received_feedback(response=feedback,)
    data.save()
    return render(request,'submitted.html')

def candidates(request):
    cand = voteoption.objects.all()
    return render(request,'candidates.html',{'candidates': cand} )

def submitvote(request):
    reg_no = request.POST['reg_no']
    selection = request.POST['selection'] 
    voter = request.POST['voter']

    if receive.objects.filter(mail=voter).exists():
        messages.info(request,'You have already Voted')
        return render(request,'submitted.html')
    else:
        data = receive(reg_no=reg_no,selection=selection,mail=voter)
        data.save()
        messages.info(request,'You have voted Successfully. Thank You!')
        return render(request,'submitted.html')

