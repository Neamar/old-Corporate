from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'docs.views.index', name='home'),
    url(r'^(?P<rule_name>[a-z-]+)$', 'docs.views.detail'),
)
