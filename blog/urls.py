from django.urls import path_re
from . import views


app_name = 'blog'

urlpatterns = [
    path_re(r'^tag/(?P<tag>[-\w]+)/', views.tag_view, name="tag"),
    path_re(r'^category/(?P<category>[-\w]+)/feed/$', views.LatestCategoryFeed(), name="category_feed"),
    path_re(r'^category/(?P<category>[-\w]+)/', views.category_view, name="category"),
    path_re(r'^author/(?P<author>[-\w]+)/', views.author_view, name="author"),
    path_re(r'(?P<blog_slug>[\w-]+)/rss.*/',
        views.LatestEntriesFeed(),
        name="latest_entries_feed"),
    path_re(r'(?P<blog_slug>[\w-]+)/atom.*/',
        views.LatestEntriesFeedAtom(),
        name="latest_entries_feed_atom"),
]
