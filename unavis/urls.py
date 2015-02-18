from django.conf.urls import patterns, url, include

from unavis import views

urlpatterns = patterns(
    '',

    url(r'^$',
        views.HomeView.as_view(), name="home"),

    url(r'^category/list/$',
        views.CategoryList.as_view(), name="category_list"),
    url(r'^category/create/$',
        views.CategoryCreate.as_view(), name="category_create"),

    url(r'^auth/', include('django.contrib.auth.urls', namespace='auth')),
)
