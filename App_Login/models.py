from pyexpat import model
from re import M
from turtle import mode
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver



# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,
    related_name='user_profile')
    profile_pic=models.ImageField(upload_to='profile_pics', blank=True)
    description=models.TextField(blank=True)
    full_name=models.CharField(max_length=264,blank=True)
    dob=models.DateField(blank=True,null=True)
    website=models.URLField(blank=True)
    facebook=models.URLField(blank=True)
    
    # def __str__(self):
    #     return '{}''{}',format(self.user.username,'profile')
    

class Follow(models.Model):
    follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')
    following=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.following
    
    
@receiver(post_save, sender=User)   
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile=UserProfile(user=instance)
        user_profile.save
        user_following=Follow(following=instance)
        user_following.save
        
        # user_following.following.add([instance.id])
        user_following.save
    



# post_save.connect(create_profile,sender=User)