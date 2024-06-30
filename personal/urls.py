from django.urls import path
from personal.views import home, about, contact, portfolio, price, services, elements, blogHome, blogSingle
urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('portfolio', portfolio, name='portfolio'),
    path('price', price, name='price'),
    path('services', services, name='services'),
    path('elements', elements, name='elements'),
    path('blog-home', blogHome, name="blog-home"),
    path('blog-single', blogSingle, name="blog-single")
]
 