from django.urls import path
from news.views import (AllNewsListView, NewsDetailView, NewsPostView, SearchNewsView, UserNewsListView)


urlpatterns = [
    # News urls
    path('all/', AllNewsListView.as_view(), name='all_news'),
    path('newspost/', NewsPostView.as_view(), name='post_a_news'),
    path('news/<uuid:news_id>/', NewsDetailView.as_view(), name='news_detail'),
    path('usernews/', UserNewsListView.as_view(), name='news_of_user'),
    path('search/', SearchNewsView.as_view(), name='search_a_news'),
]
