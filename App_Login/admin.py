from django.contrib import admin
from django.contrib.auth.models import Group,User

from App_Login.models import UserProfile
from .models import*




class profileInline(admin.StackedInline):
    model=UserProfile
    


class CustomUser(admin.ModelAdmin):
    model=User
    fields=['username']
    inlines=[profileInline]
    
    

  
admin.site.unregister(User)
admin.site.register(User,CustomUser)
  

# Register your models here.
# admin.site.unregister(User)
admin.site.register(UserProfile)
admin.site.register(Follow)

