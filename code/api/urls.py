from django.urls import path
from .views import AccountApiView, AccountDetail, GetIdGroup, PostGroup, PostGroupDetail

urlpatterns = [
    path('', AccountApiView.as_view()),
    path('account/<int:facebook_id>/', AccountDetail.as_view()),
    path('group/<int:facebook_id>/', GetIdGroup.as_view()),
    path('add_post/', PostGroup.as_view()),
    path('get_post/', PostGroupDetail.as_view()),
]