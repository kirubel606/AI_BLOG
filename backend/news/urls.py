from django.urls import path

from news.views import (AllNewsListView, ApplaudDetailView, ApplaudPostView,
                    NewsDetailView, NewsPostView, CommentDetailView,
                    CommentPostView, CommentsAggregateView, CommentsListView,
                    ReadingListDetailView, ReadingListListView,
                    ReadingListPostView, SearchNewsView, UserNewsListView)


urlpatterns = [
    # News urls
    path('all/', AllNewsListView.as_view(), name='all_news'),
    path('newspost/', NewsPostView.as_view(), name='post_a_news'),
    path('news/<uuid:news_id>/', NewsDetailView.as_view(), name='news_detail'),
    path('usernews/', UserNewsListView.as_view(), name='news_of_user'),
    path('search/', SearchNewsView.as_view(), name='search_a_news'),
    
    # news comment urls
    path('news/<uuid:news_id>/comments/all/',
         CommentsListView.as_view(), name='all_comments_of_a_news'),
    path('news/<uuid:news_id>/totalcomments/',
         CommentsAggregateView.as_view(), name='total_comments_of_a_news'),
    path('news/<uuid:news_id>/commentpost/',
         CommentPostView.as_view(), name='post_a_comment'),
    path('news/<uuid:news_id>/comment/<uuid:comment_id>/',
         CommentDetailView.as_view(), name='comment_detail'),

    # Applaud urls
    path('news/<uuid:news_id>/applaud/',
         ApplaudPostView.as_view(), name='applaud_a_news'),
    path('news/<uuid:news_id>/applauder/exists/',
         ApplaudDetailView.as_view(), name='applauder_exists'),

    # Reading-list urls
    path('news/<uuid:news_id>/readinglist/save/',
         ReadingListPostView.as_view(), name='add_to_reading_list'),
    path('readinglist/all/', ReadingListListView.as_view(), name='all_reading_list'),
    path('news/<uuid:news_id>/reader/exists/',
         ReadingListDetailView.as_view(), name='reader_exists')
]
