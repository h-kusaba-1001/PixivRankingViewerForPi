from django.urls import path
from api import views

urlpatterns = [
    path('', views.index , name='index'),
    path('get_filepaths', views.getDirectory , name='get_filepaths'),
    path('get_pixiv_ranking', views.getPixivRanking , name='get_ranking'),
    path('tweet', views.tweet , name='tweet'),
    path('get_pixiv_info', views.getPixivInfo , name='get_pixiv_info'),
]
