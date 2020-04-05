from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^news/list/$', views.post_list, name='post_list'),
    url(r'^news/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        views.post_detail, name='post_detail'),
    url(r'^news/author/$', views.author, name='author'),
    url(r'^author/send_email/$', views.send_email, name='send_email'),


]