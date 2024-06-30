from django.shortcuts import render
from personal.models import Contact, Review, Newsletter

# Create your views here.

def home(request):
    views = {}
    views["reviews"] = Review.objects.all()
    
    if request.method == "POST":
        email = request.POST["email"]
        data = Newsletter.objects.create(
            email = email
        )
        data.save()
        message = {"msg": "You will be notified for any updates."}
        return render(request, "index.html", message)
    return render(request, "index.html", views)

def about(request):
    views = {}
    views["reviews"] = Review.objects.all()
    return render(request, "about.html", views)

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

def elements(request):
    return render(request, "elements.html")

def blogHome(request):
    return render(request, "blog-home.html")

def blogSingle(request):
    return render(request, "blog-single.html")

