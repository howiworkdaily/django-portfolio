from django.contrib import admin
from django.conf import settings
from django.conf.urls.defaults import *

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    (r'^admin/(.*)', admin.site.root),
    (r'^portfolio/(.*)', include('portfolio.urls')),    
)
