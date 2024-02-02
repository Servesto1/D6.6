from django.urls import path

from .views import NewsList, PostDetail, NewsCreate, PostSearch, NewsDelete

urlpatterns =[
    path('', NewsList.as_view(), name='post_list'),
    path('', <int:pk/>, NewDetail.as_view(), name='post_detail'),
    path('search', NewsList.as_view(), name = 'post_list'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('articles/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
]