from django.urls import path
from. views import TagList

urlpatterns = [
    path('tags/', TagList.as_view(), name='tag-list'),
]