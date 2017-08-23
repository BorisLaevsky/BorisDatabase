from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login_page, name='login_page'),
    url(r'^main_page/$', views.main_page, name='main_page'),
    url(r'^worker/$', views.worker, name='worker'),
    url(r'^company/$', views.company, name='company'),
    url(r'^contracts/$', views.contracts, name='contracts'),
    url(r'^main_page/(?P<worker_passport_number>[0-9]+)/$', views.find_worker, name='find_worker'),
]
