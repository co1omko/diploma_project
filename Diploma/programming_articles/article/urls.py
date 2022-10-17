from django.urls import path

from .views import *

urlpatterns = [
    path('', ArticleHome.as_view(), name='index'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ArticleCategory.as_view(), name='category'),
    path('addpage/', AddPage.as_view(), name='add_page'),
]