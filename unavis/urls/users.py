from django.conf.urls import patterns, url

from unavis import views

urlpatterns = patterns(
    '',

    url(r'^login/$',
        views.LoginView.as_view(), name="login"),
    url(r'^logout/$',
        views.LogoutView.as_view(), name="logout"),
    url(r'^regen_password/$',
        views.RegenPasswordView.as_view(), name="regen_password"),
)
