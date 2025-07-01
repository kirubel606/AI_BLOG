from django.urls import path
from news.views import (AllNewsListView, NewsDetailView, NewsPostView, SearchNewsView, UserNewsListView,NewsRelatedView,MagazineListView)


urlpatterns = [
    # News urls
    path('all/', AllNewsListView.as_view(), name='all_news'),
    path('newspost/', NewsPostView.as_view(), name='post_a_news'),
    path('news/<uuid:news_id>/', NewsDetailView.as_view(), name='news_detail'),
    path('related/<uuid:news_id>/', NewsRelatedView.as_view(), name='news_detail'),
    path('magazine/', MagazineListView.as_view(), name='magazine_news'),
    path('usernews/', UserNewsListView.as_view(), name='news_of_user'),
    path('search/', SearchNewsView.as_view(), name='search_a_news'),
]
