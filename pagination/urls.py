from django.urls import path

from pagination import views

urlpatterns = [
    path('page-number', views.post_page_number_pagination_view, name='post-page-number-pagination-view'),
    path('limit-offset', views.post_limit_offset_pagination_view, name='post-limit-offset-pagination-view'),
    path('cursor', views.post_cursor_pagination_view, name='post-cursor-pagination-view'),
]
