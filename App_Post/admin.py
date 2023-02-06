from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import*

# unregister user here
admin.site.unregister(Group)



# Register your models here.
admin.site.register(Post)
admin.site.register(Like)