from django.shortcuts import render
from personal.models import Contact, Review

# Create your views here.

def home(request):
    views = {}
    views["reviews"] = Review.objects.all()
    return render(request, "index.html", views)

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        
        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
        # this message is for notification purpose
        message = {"msg": "Your message has been sent!"}
        return render(request, "contact.html", message)
        
    return render(request, "contact.html")
    
def portfolio(request):
    return render(request, "portfolio.html")

def services(request):
    return render(request, "services.html")

def price(request):
    return render(request, "price.html")