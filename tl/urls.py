from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView, name='detail'),
    url(r'^newtest/$', views.newtest, name='newtest'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.UpdateView, name='update'),
    url(r'^query/$', views.QueryView, name='query'),

]


# urlpatterns = [
#     url(r'^$', views.home, name='home'),
#     url(r'^newtest/$', views.testsCreateView, name='newtest'),
#     url(r'^modifytest/$', views.testsUpdateView, name='modifytest'),

# ]