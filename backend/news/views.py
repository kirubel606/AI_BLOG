import uuid

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import  News
from news.pagination import CustomPageNumberPagination
from news.serializers import (NewsSerializer)
from django.db.models import Q
from django.contrib.auth.models import Permission
from django.utils.dateparse import parse_date

class AllNewsListView(APIView):
    def get(self, request: Request) -> Response:
        filtercategory = request.query_params.get("category")
        date_from = request.query_params.get("date_from")
        date_to = request.query_params.get("date_to")
        magazine = request.query_params.get("magazine")
        iframe = request.query_params.get("iframe")
        search = request.query_params.get("search")
        query = Q(status="publish")

        if filtercategory:
            query &= Q(category=filtercategory)
        if search:
            query &= Q(title__icontains=search) | Q(title_am__icontains=search) | Q(subtitle__icontains=search)
            
        if magazine is not None:
            if magazine.lower() == "true":
                query &= Q(magazine=True)
            elif magazine.lower() == "false":
                query &= Q(magazine=False)

        if iframe is not None:
            if iframe.lower() == "true":
                query &= Q(iframe__isnull=False) & ~Q(iframe="")
            elif iframe.lower() == "false":
                query &= Q(iframe__isnull=True) | Q(iframe="")

        if date_from:
            parsed_date = parse_date(date_from)
            if parsed_date:
                query &= Q(created_at__date__gte=parsed_date)

        if date_to:
            parsed_date = parse_date(date_to)
            if parsed_date:
                query &= Q(created_at__date__lte=parsed_date)

        items = News.objects.filter(query).order_by("-created_at")

        paginator = CustomPageNumberPagination()
        return paginator.generate_response(items, request)

class SidebarNewsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request: Request) -> Response:
        # You can customize the number and filters here
        sidebar_news = News.objects.filter(status='publish').order_by('-created_at')[:10]
        serializer = NewsSerializer(sidebar_news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MajorNewsListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request: Request) -> Response:
        major_news = News.objects.filter(status='publish').order_by('-created_at')
        total = major_news.count()
        paginator = CustomPageNumberPagination()
        return paginator.generate_response(major_news, NewsSerializer, request, total)

class MagazineListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        magazines = News.objects.filter(status='publish', magazine=True).order_by('-created_at')
        paginator = CustomPageNumberPagination()
        return paginator.generate_response(magazines, request)

    
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
        if not request.user.has_perm('news.add_news'):
            return Response(
                {"detail": "You do not have permission to add news."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Make request.data mutable safely
        data = request.data.dict()  # returns normal dict, but loses FILES!
        
        # Better: use request.data as-is and override validated_data in serializer if needed
        serializer = NewsSerializer(
            data=request.data,
            context={'request': request}
        )
        
        # Attach user id during serializer save instead
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)  # Better to pass instance or field
            return Response(
                data={'message': 'News created successfully', 'news': serializer.data},
                status=status.HTTP_201_CREATED
            )

        return Response(data={'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class UserNewsListView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        news_status = request.query_params.get('status', None)

        if not news_status :
            return Response(data={'message': 'Query param `status` is not provided'}, status=status.HTTP_400_BAD_REQUEST)
        if news_status  == 'all':
            if request.user.is_admin:
                news = News.objects.all()
            else:
                news = News.objects.filter(author=request.user.id)
        if news_status == 'draft':
            if request.user.is_admin:
                news = News.objects.filter(status=news_status)
            else:
                news = News.objects.filter(
                    author=request.user.id, status=news_status)
        elif news_status == 'publish':
            if request.user.is_admin:
                news = News.objects.filter(status=news_status)
            else:
                news = News.objects.filter(
                    author=request.user.id, status=news_status)

        news_serializer = NewsSerializer(instance=news, many=True)
        return Response(data=news_serializer.data, status=status.HTTP_200_OK)


class NewsDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request: Request, news_id: uuid) -> Response:
        try:
            news = News.objects.get(pk=news_id)
            # Increment view count
            news.view_count += 1
            news.save(update_fields=['view_count'])
            news_serializer = NewsSerializer(instance=news)
            return Response(data=news_serializer.data, status=status.HTTP_200_OK)
        except News.DoesNotExist:
            return Response(data={'message': 'News does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request: Request, news_id: uuid) -> Response:
        try:
            if not request.user.has_perm('news.change_news'):  # replace `yourapp` with your actual app label
                return Response(
                    {"detail": "You do not have permission to edit news."},
                    status=status.HTTP_403_FORBIDDEN
                )
            news = News.objects.get(pk=news_id)

            if news.author.id != request.user.id:
                return Response(data={'message': 'You are unauthorized to update the requested news'}, status=status.HTTP_401_UNAUTHORIZED)

            news_serializer = NewsSerializer(
                instance=news, data=request.data, partial=True)
            news_serializer = NewsSerializer(
                instance=news,
                data=request.data,
                partial=True,
                context={'request': request}
            )
            if news_serializer.is_valid(raise_exception=True):
                news_serializer.save()
                return Response(data={'message': 'News updated successfully', 'news': news_serializer.data}, status=status.HTTP_200_OK)

            return Response(data=news_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except News.DoesNotExist:
            return Response(data={'message': 'News does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, news_id: uuid) -> Response:
        try:
            if not request.user.has_perm('news.delete_news'):  # replace `yourapp` with your actual app label
                return Response(
                    {"detail": "You do not have permission to delete news."},
                    status=status.HTTP_403_FORBIDDEN
                )
            news = News.objects.get(pk=news_id)

            if news.author.id != request.user.id:
                return Response(data={'message': 'You are unauthorized to delete the requested news'}, status=status.HTTP_401_UNAUTHORIZED)

            news.delete()
            return Response(data={'message': 'News deleted successfully'}, status=status.HTTP_200_OK)
        except News.DoesNotExist:
            return Response(data={'message': 'News does not exist'}, status=status.HTTP_404_NOT_FOUND)


class NewsRelatedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, news_id):
        try:
            main_news = News.objects.get(pk=news_id)
        except News.DoesNotExist:
            return Response({'message': 'News not found'}, status=status.HTTP_404_NOT_FOUND)

        # Split tags by comma and trim whitespace
        tag_list = [tag.strip().lower() for tag in (main_news.tags or "").split(",") if tag.strip()]

        # Build query
        related_news = News.objects.filter(
            Q(category=main_news.category) |
            Q(tags__iregex=r'(' + '|'.join(tag_list) + ')')
        ).exclude(id=news_id).distinct().order_by('-created_at')[:10]  # Limit to 10 related

        serializer = NewsSerializer(related_news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

