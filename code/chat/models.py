from django.db import models

# Create your models here.


class AccountFacebook(models.Model):
    username = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=255, default="")
    userid = models.CharField(max_length=255, default="")
    cookie = models.TextField(default="")
    token = models.TextField(default="")
    name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name

class GroupFacebook(models.Model):
    account_facebook = models.ForeignKey(AccountFacebook, on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=150, default="")
    privacy = models.CharField(max_length=10, default="")
    group_id = models.CharField(max_length=25, default="")

    def __str__(self):
        return self.name 

class PostFacebook(models.Model):
    account_facebook = models.ForeignKey(AccountFacebook, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255, default='')
    content = models.CharField(max_length=150, default='')
    group_id = models.CharField(max_length=255, default='')
    file = models.FileField('post', upload_to='image',
                            blank=True, null=True, default='')
    added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id}'

class ImagePost(models.Model):
    post_id = models.ForeignKey(PostFacebook, on_delete=models.CASCADE, related_name='images')
    file = models.FileField(upload_to='image',
                            blank=True, null=True, default='')
