import uuid

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import  News
from news.pagination import CustomPageNumberPagination
from news.serializers import (NewsSerializer)


class AllNewsListView(APIView):

    def get(self, request: Request) -> Response:
        category: str = request.query_params.get('category', None)

        if category:
            news = News.objects.filter(status='publish', category=category)
        else:
            news = News.objects.filter(status='publish')

        total = news.count()
        paginator = CustomPageNumberPagination()
        return paginator.generate_response(news, NewsSerializer, request, total)


class SearchNewsView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        search_term: str = request.query_params.get('title', None)

        if not search_term:
            return Response(data={'message': 'query_param "title" is not provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        filtered_news = News.objects.filter(title__icontains=search_term)
        news_serializer = NewsSerializer(instance=filtered_news, many=True)
        return Response(data=news_serializer.data, status=status.HTTP_200_OK)
    

class NewsPostView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request: Request) -> Response:
        data = request.data.copy()
        data['author'] = str(request.user.id)

        news_serializer = NewsSerializer(data=data)
        if news_serializer.is_valid(raise_exception=True):
            news_serializer.save()
            return Response(data={'message': 'News created successfully', 'news': news_serializer.data}, status=status.HTTP_201_CREATED)

        return Response(data={'message': news_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserNewsListView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        news_status = request.query_params.get('status', None)

        if not news_status:
            return Response(data={'message': 'Query param `status` is not provided'}, status=status.HTTP_400_BAD_REQUEST)

        if news_status == 'draft':
            news = News.objects.filter(
                author=request.user.id, status=news_status)
        elif news_status == 'publish':
            news = News.objects.filter(
                author=request.user.id, status=news_status)

        news_serializer = NewsSerializer(instance=news, many=True)
        return Response(data=news_serializer.data, status=status.HTTP_200_OK)


class NewsDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request: Request, news_id: uuid) -> Response:
        try:
            news = News.objects.get(pk=news_id)
            news_serializer = NewsSerializer(instance=news)
            return Response(data=news_serializer.data, status=status.HTTP_200_OK)
        except News.DoesNotExist:
            return Response(data={'message': 'News does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request: Request, news_id: uuid) -> Response:
        try:
            news = News.objects.get(pk=news_id)

            if news.author.id != request.user.id:
                return Response(data={'message': 'You are unauthorized to update the requested news'}, status=status.HTTP_401_UNAUTHORIZED)

            news_serializer = NewsSerializer(
                instance=news, data=request.data, partial=True)
            if news_serializer.is_valid(raise_exception=True):
                news_serializer.save()
                return Response(data={'message': 'News updated successfully', 'news': news_serializer.data}, status=status.HTTP_200_OK)

            return Response(data=news_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except News.DoesNotExist:
            return Response(data={'message': 'News does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, news_id: uuid) -> Response:
        try:
            news = News.objects.get(pk=news_id)

            if news.author.id != request.user.id:
                return Response(data={'message': 'You are unauthorized to delete the requested news'}, status=status.HTTP_401_UNAUTHORIZED)

            news.delete()
            return Response(data={'message': 'News deleted successfully'}, status=status.HTTP_200_OK)
        except News.DoesNotExist:
            return Response(data={'message': 'News does not exist'}, status=status.HTTP_404_NOT_FOUND)
