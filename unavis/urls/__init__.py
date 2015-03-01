from django.conf.urls import patterns, url, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

from django.views import i18n as i18n_views
from unavis import views

urlpatterns = i18n_patterns(
    '',

    url(r'^$',
        views.HomeView.as_view(), name="home"),

    url(r'^language/set/$',
        i18n_views.set_language, name="set_language"),

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
