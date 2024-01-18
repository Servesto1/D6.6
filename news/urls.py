from django.urls import path

from .views import NewsList

urlpatterns =[
    path('', NewsList.as_view(), name='post_list'),
    path('', <int;pk/>, NewDetail.as_view(), name='post_detail'),
]