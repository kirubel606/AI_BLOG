from rest_framework import pagination, status
from rest_framework.exceptions import NotFound as NotFoundError
from rest_framework.request import Request
from rest_framework.response import Response
from news.serializers import NewsSerializer

from math import ceil


class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 6  # Still keep this for reference
    page_query_param = 'page'

    def generate_response(self, items, request: Request) -> Response:
        page_number = int(request.query_params.get(self.page_query_param, 1))

        # Split items into news and videos
        news_items = [item for item in items if not item.iframe]
        video_items = [item for item in items if item.iframe]

        # Build pages with 2 news + 1 video per page
        per_page = 3
        grouped_items = []

        max_groups = max(
            ceil(len(news_items) / 2),
            len(video_items)
        )

        for i in range(max_groups):
            group = []
            news_start = i * 2
            video_start = i

            # Add up to 2 news
            group.extend(news_items[news_start:news_start + 2])
            # Add 1 video
            if video_start < len(video_items):
                group.append(video_items[video_start])

            grouped_items.extend(group)

        # Paginate final grouped list
        self.page_size = per_page
        try:
            page = self.paginate_queryset(grouped_items, request)
        except pagination.NotFound:
            return Response(
                {"message": "No results found for the requested page"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = NewsSerializer(page, many=True)
        return self.get_paginated_response({
            "result": serializer.data,
            "total_pages": ceil(len(grouped_items) / per_page),
        })



