from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from key import setting

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url('^blog/',include('blog.urls')),
	url('^',include('blog.urls')),
	url('^accountbook/',include('accountbook.urls')),
)

handler404 = 'blog.views.handle404'
handler500 = 'blog.views.handle500'
