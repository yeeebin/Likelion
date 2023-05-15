from django.db import models
#from django.conf import settings
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tagline = models.CharField(max_length=50, blank = True, null = True)

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag
    

class Post(models.Model): # pk값 지정 안 하면 Django가 알아서 판단하고 생성
    title = models.CharField(max_length=50)
    body =  models.TextField()
    date = models.DateTimeField(auto_now_add=True) #괄호 안에 옵션
    tags = models.ManyToManyField(Tag)
    location = models.CharField(max_length=50, blank = True, null = True)

    def __str__(self):
        return self.title
    

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}가 {self.blog.title}을 즐겨찾기에 등록했습니다."


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}님이 '{self.blog.title}'글에 공감합니다. "
    

class Category(models.Model):
    category = models.CharField(primary_key=True, max_length=20, unique=True)
    post = models.ForeignKey(Post, max_length=20, on_delete=models.CASCADE)

    def __str__(self):
        return self.category


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE) 

    def __str__(self):
        return self.comment





