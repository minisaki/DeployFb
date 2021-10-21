from rest_framework import serializers
from chat.models import AccountFacebook, GroupFacebook, PostFacebook, ImagePost

class ImagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePost
        fields = '__all__'


class PostFacebookSerializer(serializers.ModelSerializer):
    images = ImagePostSerializer(many=True)
    class Meta:
        model = PostFacebook
        fields = ['id','account_facebook','title', 'content', 'file', 'group_id', 'added', 'images']


class GroupFacebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupFacebook
        fields = ['account_facebook', 'name', 'privacy', 'group_id']


class AccountSerializer(serializers.ModelSerializer):
    groups = GroupFacebookSerializer(many=True)

    class Meta:
        model = AccountFacebook        
        fields = ['id', 'username', 'password', 'userid', 'cookie', 'token', 'name', 'groups']

