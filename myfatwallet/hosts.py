from django_hosts import patterns, host


host_patterns = patterns('',
    host(r'api', 'api.urls', name='api'),
    host(r'app', 'app.urls', name='app'),
    host(r'www', 'website.urls', name='www'),
    host(r'', 'website.urls', name='default')
)