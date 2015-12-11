from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from myfatwallet import settings


urlpatterns = patterns('website.views',
    url(r'^auth/signin/$', 'auth_signin', name='website-signin'),
    url(r'^auth/signup/$', 'auth_signup', name='website-signup'),
    url(r'^$', 'get_main', name='website-main')
)
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)