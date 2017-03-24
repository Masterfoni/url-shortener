from django.conf.urls import patterns, include, url
 
urlpatterns = patterns('shortenersite.views',
    url(r'^$', 'index', name='home'),
 
    url(r'^(?P<short_id>\w{6})$', 'redirect_original', name='redirectoriginal'),
 
    url(r'^makeshort/$', 'shorten_url', name='shortenurl'),
)