from django.urls import path
from .views import PostList, PostDetail, PostSearch, NewsCreate, NewsUpdate, PostDelete, ArticleCreate, ArticleUpdate, \
   ArticleDelete, CategoryList, subscribe, HelloView
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('', PostList.as_view(), name='all_news'),
   path('<int:pk>', PostDetail.as_view(), name='news_detail'),
   path('search/', cache_page(30)(PostSearch.as_view()), name='post_search'),
   path('news/create/', NewsCreate.as_view(), name='create_news'),
   path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='update_news'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='delete_news'),
   path('articles/create/', ArticleCreate.as_view(), name='create_article'),
   path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='update_article'),
   path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='delete_article'),
   path('categories/<int:pk>', CategoryList.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
   path('hello', HelloView.as_view(), name='hello'),
]
