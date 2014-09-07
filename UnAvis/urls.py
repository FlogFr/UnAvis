"""
Urls module
"""

from django.conf.urls import patterns, include, url

from UnAvis import views

urlpatterns = patterns(
    '',

    #
    url(r'^$',
        views.HomeView.as_view(), name="home"),


    url(r'^auth/signup',
        views.SignUpView.as_view(), name="signup"),
    url(r'^auth/',
        include('django.contrib.auth.urls',
                namespace='Auth')),
    url(r'^',
        include('django.contrib.flatpages.urls',
                namespace='flatpages')),
)
