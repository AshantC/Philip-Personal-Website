from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
class Review(models.Model):
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=400)
    image = models.TextField(blank=True)
    review = models.TextField()
    
    def __str__(self):
        return f"{self.name}  {self.post}"
    
class Newsletter(models.Model):
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.email
    