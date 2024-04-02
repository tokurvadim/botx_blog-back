from django.db import models

class User(models.Model):
    access_token = models.CharField(primary_key=True, max_length=60, unique=True)
    short_name = models.CharField(max_length=32)
    author_name = models.CharField(max_length=128, null=True)
    author_uri = models.CharField(max_length=512, null=True)

class Page(models.Model):
    id = models.BigAutoField(primary_key=True)
    path = models.SlugField(max_length=256, unique=True)
    title = models.SlugField(max_length=256)
    author_name = models.ForeignKey(to='User', on_delete=models.CASCADE, max_length=60)
    content = models.BinaryField(max_length=65792)
    created_at = models.DateField(auto_now_add=True)
    last_changed_at = models.DateField(auto_now=True)
    views = models.IntegerField(default=0)

class Page_Category(models.Model):
    page = models.ForeignKey(to='Page', on_delete=models.CASCADE)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    parent_id = models.ForeignKey(to='self', on_delete=models.CASCADE, null=True)

class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    page = models.ForeignKey(to='Page', on_delete=models.CASCADE)
    access_token = models.ForeignKey(to='User', on_delete=models.CASCADE)
    content = models.CharField(max_length=256, null=False)
    created_at = models.DateField(auto_now_add=True)
    last_changed_at = models.DateField(auto_now=True)
    parent_id = models.ForeignKey(to='self', null=True, on_delete=models.CASCADE)
