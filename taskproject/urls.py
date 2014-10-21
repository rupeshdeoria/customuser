from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from quickstart import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)

from book import views
from myauth import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'taskproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    #url(r'^book/$', views.BookView.as_view(), name='book-list'),
    url(r'^userslist/$', views.UserView.as_view(), name='user-list'),
)
