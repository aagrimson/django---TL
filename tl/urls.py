from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^newtest/$', views.newtest, name='newtest'),
    url(r'^modifytest/$', views.modifytest, name='modifytest'),

]


# urlpatterns = [
#     url(r'^$', views.home, name='home'),
#     url(r'^newtest/$', views.testsCreateView, name='newtest'),
#     url(r'^modifytest/$', views.testsUpdateView, name='modifytest'),

# ]