from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userprofileinfo(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)

    portfolio_site = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to = 'app_five',blank = True)

    def __str__(self):
        return self.user.username

'''
#Create models
class Userprofileinfo_user(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.user.email

class Userprofileinfo_addon(models.Model):
    user_info = models.ForeignKey(Userprofileinfo_user,on_delete = models.CASCADE)
    ph = models.IntegerField()
    Address1 = models.CharField()
    Address2 = models.CharField()
    Address3 = models.CharField()
    city = models.CharField()
    state = models.CharField()
    zip = models.IntergerField()
    gender = models.CharField()

    def __str__(self):
        return self.user.email
'''
