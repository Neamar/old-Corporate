from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'doc.views.index', name='home'),
    url(r'^(?P<rule_name>[a-z-]+)$', 'doc.views.detail'),
)
