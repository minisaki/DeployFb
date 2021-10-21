
from chat.models import AccountFacebook, GroupFacebook, PostFacebook, ImagePost
from .serializers import AccountSerializer, GroupFacebookSerializer, PostFacebookSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
# class AccountApiView(generics.ListAPIView):
#     queryset = AccountFacebook.objects.all()
#     serializer_class = AccountSerializer


class AccountApiView(APIView):

    def get(self, request):
        account_fb = AccountFacebook.objects.all()
        serializer = AccountSerializer(account_fb, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetail(APIView):

    def get_object(self, facebook_id):
        try:
            return AccountFacebook.objects.get(userid=facebook_id)
        except AccountFacebook.DoesNotExist:
            raise Http404

    def get(self, request, facebook_id):
        print('vao dayxx')
        account = self.get_object(facebook_id)
        serializer = AccountSerializer(account)
        url = f"https://graph.facebook.com/v12.0/{facebook_id}/groups/?pretty=0&limit=100&access_token=" \
              f"{serializer.data['token']}"
        r = requests.get(url)
        text = r.json()
        # print(type(text))
        print(text['data'])
        # f = open("./group.txt", "r")
        # text = f.read()
        # f.close()
        # print(text)
        for data in text['data']:
            GroupFacebook.objects.create(account_facebook=account, name=data['name'],
                                         privacy=data['privacy'], group_id=data['id'])

        return Response(serializer.data)


class GetIdGroup(APIView):

    def get_object(self, facebook_id):
        try:
            account_fb = AccountFacebook.objects.get(userid=facebook_id)
            return account_fb
        except AccountFacebook.DoesNotExist:
            raise Http404

    def get(self, request, facebook_id):
        account = self.get_object(facebook_id)
        serializer = AccountSerializer(account)       
        return Response(serializer.data)


class PostGroup(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    # parser_classes = [JSONParser]

    def get_object(self, facebook_id):
        try:
            return AccountFacebook.objects.get(userid=facebook_id)
        except AccountFacebook.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        id = request.query_params.get('fb_id')
        account = self.get_object(id)
        all_images = PostFacebook.objects.filter(account_facebook=account)
        serializer = PostFacebookSerializer(all_images, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # print(request.data)
        fb_id = request.data['fb_id']
        account = self.get_object(fb_id)
        print(account)
        images = request.data.getlist('files')
        print(images)
        post = PostFacebook.objects.create(account_facebook=account, content=request.data['content'], group_id=request.data['group_id'])
        for image in images:
            image_post = ImagePost.objects.create(post_id=post, file=image)
        # file_serializer = PostFacebookSerializer(post, many=False)
        return Response('ok')
        # return Response(file_serializer.data, status=status.HTTP_201_CREATED)

class PostGroupDetail(APIView):

    def get(self, request):
        id_post = request.query_params.get('id_post')
        post = PostFacebook.objects.get(id=id_post)
        serializer = PostFacebookSerializer(post)
        return Response(serializer.data)
