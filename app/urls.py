from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from myfatwallet import settings


urlpatterns = patterns('app.views',
    url(r'^api/', include('api.urls')),
    url(r'^signout/', 'get_signout', name='app-signout'),
    url(r'^confirm/(?P<pk>[-\w]+)', 'get_confirm', name='app-confirm'),
    url(r'^inventory/(?P<pk>[-\w]+)', 'get_inventory', name='app-inventory'),
    url(r'^inventory-management', 'manage_inventory', name='app-inventory-management'),
    url(r'^transaction/(?P<pk>\d+)', 'get_transaction', name='app-transaction'),
    url(r'^$', 'get_main', name='app-main'),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    