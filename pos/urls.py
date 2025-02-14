from django.urls import path
from . import views
urlpatterns=[
    path('',views.myfunctionc,name="index"),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('deletevideo/<int:pk>/',views.deletevideo,name='deletevideo'),
    path('video_load',views.video_load,name='video_load'),
    path('video/<int:pk>/',views.videoplay,name='videoplay'),
    path('user_details',views.user_details,name='user_details'),
    path('video_category',views.video_category,name='video_category')
]