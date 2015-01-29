from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from bitsulting import views
from bitsulting.models import Question, Category

urlpatterns = patterns('',
    url(r'^$', views.new_home, name='index'),
    #url(r'^login/$', login),
    #url(r'^logout/$', logout,{'next_page': 'index'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^q/(?P<slug>[^\.]+)', views.view_question, name='q'),
    url(r'^c/(?P<slug>[^\.]+)', views.view_category, name='c'),
)