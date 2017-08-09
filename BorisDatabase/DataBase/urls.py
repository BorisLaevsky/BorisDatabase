from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^worker/', views.worker, name='worker'),
    url(r'^company/', views.company, name='company'),
    url(r'^contracts/', views.contracts, name='contracts'),
]
