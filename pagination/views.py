from rest_framework import mixins, viewsets

from domain.models import Post
from pagination.paginations import CustomPageNumberPagination, CustomCursorPagination, CustomLimitOffsetPagination
from pagination.serializers import PostSerializer


class PostPageNumberPaginationAPI(mixins.ListModelMixin, viewsets.GenericViewSet):
    pagination_class = CustomPageNumberPagination
    serializer_class = PostSerializer
    queryset = Post.objects.all()


post_page_number_pagination_view = PostPageNumberPaginationAPI.as_view({'get': 'list'})


class PostLimitOffsetPaginationAPI(mixins.ListModelMixin, viewsets.GenericViewSet):
    pagination_class = CustomLimitOffsetPagination
    serializer_class = PostSerializer
    queryset = Post.objects.all()


post_limit_offset_pagination_view = PostLimitOffsetPaginationAPI.as_view({'get': 'list'})


class PostCursorPaginationAPI(mixins.ListModelMixin, viewsets.GenericViewSet):
    pagination_class = CustomCursorPagination
    serializer_class = PostSerializer
    queryset = Post.objects.all()


post_cursor_pagination_view = PostCursorPaginationAPI.as_view({'get': 'list'})
