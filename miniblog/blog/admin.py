from django.contrib import admin
from .models import post
# Register your models here.
@admin.register(post)
class PostModelAdmin(admin.ModelAdmin):
    list_displsy =['id','title','desc']