"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib.auth.decorators import login_required
from django.conf.urls import include, url
from django.contrib import admin

from blog.views import PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, index
# AjaxPhotoUploadView,     url(r'^(?P<pk>\d+)/ajax-upload/$', AjaxPhotoUploadView.as_view(), name='ajax_photo_upload_view',),

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create/$', login_required(PostCreateView.as_view()), name='create'),
    url(r'^$', index, name='list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>[0-9]+)/$', login_required(PostUpdateView.as_view()), name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', login_required(PostDeleteView.as_view()), name='delete'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
]
