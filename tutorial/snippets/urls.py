from django.urls import path,re_path
from snippets import views

urlpatterns=[
    path('',views.api_root),

    re_path(r'^snippets/$',
        views.SnippetList.as_view(),
        name='snippet-list'),

    re_path(r'^snippets/(?P<pk>[0-9]+)/$',
            views.SnippetDetail.as_view(),
            name='snippet-detail'),

    re_path(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
            views.SnippetHighlight.as_view(),
            name='snippet-highlight'),

    re_path(r'^users/$',
            views.UserList.as_view(),
            name='user-list'),

    re_path(r'^users/(?P<pk>[0-9]+)/$',
            views.UserDetail.as_view(),
            name='user-detail'),

]