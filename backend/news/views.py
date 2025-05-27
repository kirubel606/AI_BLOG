import uuid

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Applaud, News, Comment, ReadingList
from news.pagination import CustomPageNumberPagination
from news.serializers import (ApplaudSerializer, NewsSerializer, CommentSerializer,
                          ReadingListSerializer)


# ------------------------------ News views ------------------------------
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

            news_serializer = Newserializer(
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


# ------------------------------ Comment views ------------------------------
class CommentsListView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, news_id: uuid) -> Response:
        comments = Comment.objects.filter(news=news_id)
        comment_serializer = CommentSerializer(instance=comments, many=True)
        return Response(data=comment_serializer.data, status=status.HTTP_200_OK)


class CommentsAggregateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, news_id: uuid) -> Response:
        total = Comment.objects.filter(news=news_id).count()
        return Response(data={'total': total}, status=status.HTTP_200_OK)
    

class CommentPostView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, news_id: uuid) -> Response:
        try:
            news = News.objects.get(pk=news_id)
            
            data = {}
            data['news'] = str(news_id)
            data['user'] = str(request.user.id)
            data['content'] = request.data

            comment_serializer = CommentSerializer(data=data)
            if comment_serializer.is_valid(raise_exception=True):
                comment_serializer.save()
                return Response(data={'message': 'Comment posted successfully', 'comment': comment_serializer.data}, status=status.HTTP_201_CREATED)

            return Response(data=comment_serializer.data, status=status.HTTP_400_BAD_REQUEST)
        except News.DoesNotExist:
            return Response(data={'message': 'News does not exist'}, status=status.HTTP_404_NOT_FOUND)


class CommentDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request: Request, news_id: uuid, comment_id: uuid) -> Response:
        try:
            news = News.objects.get(pk=news_id)
            comment = Comment.objects.get(pk=comment_id)

            if request.user.id != comment.user.id:
                return Response(data={'message': 'You are unauthorized to update the requested comment'}, status=status.HTTP_401_UNAUTHORIZED)

            comment_serializer = CommentSerializer(
                instance=comment, data=request.data, partial=True)
            if comment_serializer.is_valid(raise_exception=True):
                comment_serializer.save()
                return Response(data={'message': 'Comment updated successfully'}, status=status.HTTP_200_OK)

            return Response(data=comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except (News.DoesNotExist, Comment.DoesNotExist) as e:
            if isinstance(e, News.DoesNotExist):
                return Response(data={'message': 'News does not exist'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(data={'message': 'Comment does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, news_id: uuid, comment_id: uuid) -> Response:
        try:
            news = News.objects.get(pk=news_id)
            comment = Comment.objects.get(pk=comment_id)
            comment.delete()
            return Response(data={'message': 'Comment deleted successfully'}, status=status.HTTP_200_OK)
        except (News.DoesNotExist, Comment.DoesNotExist) as e:
            if isinstance(e, News.DoesNotExist):
                return Response(data={'message': 'News does not exist'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(data={'message': 'Comment does not exist'}, status=status.HTTP_404_NOT_FOUND)


# ------------------------------ Applaud views ------------------------------
class ApplaudPostView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, news_id: uuid) -> Response:
        try:
            news = News.objects.get(pk=news_id)
            user_applauded = Applaud.objects.filter(
                news=news_id, user=request.user.id).exists()
            if user_applauded:
                news.applaud_count -= 1
                Applaud.objects.filter(
                    news=news_id, user=request.user.id).delete()
            else:
                news.applaud_count += 1
                data = {
                    'news': news_id,
                    'user': request.user.id
                }

                applaud_serializer = ApplaudSerializer(data=data)
                if applaud_serializer.is_valid(raise_exception=True):
                    applaud_serializer.save()

            news.save()
            news_serializer = NewsSerializer(instance=news)
            return Response(data=news_serializer.data, status=status.HTTP_200_OK)

        except News.DoesNotExist:
            return Response(data={'message': 'News does not exist'}, status=status.HTTP_404_NOT_FOUND)


class ApplaudDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, news_id: uuid) -> Response:
        if Applaud.objects.filter(news=news_id, user=request.user.id).exists():
            return Response(data={'message': 'true'}, status=status.HTTP_200_OK)

        return Response(data={'message': 'false'}, status=status.HTTP_200_OK)


# ------------------------------ Reading-list related views ------------------------------
class ReadingListPostView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, news_id: uuid) -> Response:
        try:
            news = News.objects.get(pk=news_id)
            user_saved = ReadingList.objects.filter(
                news=news_id, user=request.user.id).exists()
            if user_saved:
                ReadingList.objects.filter(
                    news=news_id, user=request.user.id).delete()
                return Response(data={'message': 'News removed from the reading-list successfully'}, status=status.HTTP_200_OK)
            else:
                data = {
                    'news': news_id,
                    'user': request.user.id
                }

                reading_list_serializer = ReadingListSerializer(data=data)
                if reading_list_serializer.is_valid(raise_exception=True):
                    reading_list_serializer.save()

                return Response(data={'message': 'News added to the reading-list successfully'}, status=status.HTTP_200_OK)
        except News.DoesNotExist:
            return Response(data={'message': 'News does not exist'}, status=status.HTTP_404_NOT_FOUND)


class ReadingListDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, news_id: uuid) -> Response:
        if ReadingList.objects.filter(news=news_id, user=request.user.id).exists():
            return Response(data={'message': 'true'}, status=status.HTTP_200_OK)

        return Response(data={'message': 'false'}, status=status.HTTP_200_OK)


class ReadingListListView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        try:
            user = get_user_model().objects.get(pk=request.user.id)
            reading_list = ReadingList.objects.filter(user=request.user.id)
            reading_list_serializer = ReadingListSerializer(
                reading_list, many=True)
            return Response(data=reading_list_serializer.data, status=status.HTTP_200_OK)

        except get_user_model().DoesNotExist:
            return Response(data={'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
