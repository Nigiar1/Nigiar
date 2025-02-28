from django.urls import path
from .views import index, post, get_category

urlpatterns = [
    path('', index, name='home'),
    path('post/<slug:slug>/', post, name='post_detail'),
    path('category/<slug:slug>/', get_category, name='category_detail'),
]