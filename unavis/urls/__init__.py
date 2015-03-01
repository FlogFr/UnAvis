from django.conf.urls import patterns, url, include
from django.conf import settings

from unavis import views

urlpatterns = patterns(
    '',

    url(r'^$',
        views.HomeView.as_view(), name="home"),

    url(r'^category/list/$',
        views.CategoryList.as_view(), name="category_list"),
    url(r'^category/create/$',
        views.CategoryCreate.as_view(), name="category_create"),

    url(r'^users/', include('unavis.urls.users', namespace='users')),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns(
        '',
        url(r'^rosetta/', include('rosetta.urls')),
    )
