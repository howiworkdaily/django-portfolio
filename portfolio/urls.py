from django.conf.urls.defaults import *
from django.contrib import admin
from views import project_detail, category_detail, category_list, skill_detail

admin.autodiscover()

urlpatterns = patterns(
    '',

    url(
        regex = r'^$',
        view = category_list,
        name = 'category_list',
        ),

    url(
        regex = r'^category/(?P<slug>[-\w]+)/$',
        view = category_detail,
        name = 'category_detail',
        ),

    url(
        regex = r'^project/(?P<slug>[-\w]+)/$',
        view = project_detail,
        name = 'project_detail',
        ),

    url(
        regex = r'^skill/(?P<slug>[-\w]+)/$',
        view = skill_detail,
        name = 'skill_detail',
        ),       
)
