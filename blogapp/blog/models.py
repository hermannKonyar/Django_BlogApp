from django.db import models



class BlogEntry(models.Model):
    title=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    description=models.TextField()
    entry=models.TextField()
    isActive=models.BooleanField()
    isHome=models.BooleanField()

class FoodBlog(models.Model):
    title=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    description=models.TextField()
    entry=models.TextField()
    isActive=models.BooleanField()
    isHome=models.BooleanField()

class UserInfo(models.Model):
    name=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    description =models.TextField()
    isActive=models.BooleanField()
    
    
class Videos(models.Model):
    title=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    url=models.TextField()
    imageUrl=models.TextField()
    description=models.TextField()
    isActive=models.BooleanField()
    


