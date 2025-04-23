from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        'variable1' :"This is sent",
        'variable2' :"This is sent which is variable2",
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')
   # return HttpResponse("This is About Page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is Service page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')
    return render(request, 'contact.html')
    #return HttpResponse("This is Contact page")

def home(request):
    return render(request, 'index.html')
    #return HttpResponse("This is Home page")