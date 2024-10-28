from django.db import models

class Register(models.Model):
    username = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=25,null=False)
    mobile_number = models.IntegerField(null=False)
    password = models.CharField(max_length=25,null=False)
    confirm_password = models.CharField(max_length=25,null=False)

    def __str__(self):
        return self.username

class Login(models.Model):
    username = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=25,null=False)

    def __str__(self):
        return self.username
    
class Movie(models.Model):
    moviename = models.CharField(max_length=100,null=False)
    theatrescreen = models.CharField(max_length=100,null=False)
    image = models.ImageField(upload_to="images",null=False,blank=False)

    def __str__(self):
        return self.moviename