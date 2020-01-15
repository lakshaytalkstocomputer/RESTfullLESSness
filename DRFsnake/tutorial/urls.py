from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/',views.snippet_detail)
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)

from .views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
#
# snippet_list = SnippetViewSet.as_view({
#     'get' : 'list',
#     'post': 'create',
# })
#
#
# snippet_detail = SnippetViewSet.as_view({
#     'get' : 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delelte':'destroy'
# })
#
# snippet_highlight = SnippetViewSet.as_view({
#     'get':'highlight',
# }, renderer_classes = [renderers.StaticHTMLRenderer])
#
# user_list = UserViewSet.as_view({
#     'get':'list'
# })
#
# user_detail = UserViewSet.as_view({
#     'get':'retrieve'
# })
#

#
# urlpatterns = format_suffix_patterns([
#     path('', views.api_root),
#     path('snippets/',
#          snippet_list,
#          name='snippet-list'),
#     path('snippets/<int:pk>/',
#          snippet_detail,
#          name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/',
#         snippet_highlight,
#         name = 'snippet-highlight'),
#     path('users/',
#          user_list,
#          name = 'user-list'),
#     path('users/<int:pk>/',
#          user_detail,
#          name = 'user-detail'),
# ])
#
# #urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'user',views.UserViewSet)

urlpatterns = [path('', include(router.urls))]
