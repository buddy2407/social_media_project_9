from django.urls import path
from social_appe.views import Postlist,PostDetailView,PostEditView,PostDeleteView,CommentDeleteView,ProfileView,ProfileEditView,AddFollowers,RemoveFollowers,AddLike,AddDislike,UserSearch

urlpatterns = [
    path('',Postlist.as_view(),name='post_list'),
    path('post/<int:pk>',PostDetailView.as_view(),name="post_details"),
    path('post/edit/<int:pk>',PostEditView.as_view(),name='post_edit'),
    path('post/delete/<int:pk>',PostDeleteView.as_view(),name='post_delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>',CommentDeleteView.as_view(),name='comment_delete'),
    path('post/<int:pk>/like',AddLike.as_view(),name='like'),
    path('post/<int:pk>/dislike',AddDislike.as_view(),name='dislike'),
    path('profile/<int:pk>',ProfileView.as_view(),name='profile'),
    path('profile/edit/<int:pk>',ProfileEditView.as_view(),name='profile_edit'),
    path('profile/<int:pk>/followers/add',AddFollowers.as_view(),name='add_followers'),
    path('profile/<int:pk>/followers/remove',RemoveFollowers.as_view(),name='remove_followers'),
    path('search/',UserSearch.as_view(),name='profile_search')
]