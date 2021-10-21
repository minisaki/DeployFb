from django.contrib import admin

# Register your models here.
from .models import AccountFacebook, GroupFacebook, PostFacebook, ImagePost


admin.site.register(AccountFacebook)
admin.site.register(GroupFacebook)
admin.site.register(PostFacebook)
admin.site.register(ImagePost)