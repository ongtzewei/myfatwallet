from api import views
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from myfatwallet import settings


router = routers.SimpleRouter()
router.register(r'search',views.search.SearchViewSet,base_name='search')
urlpatterns = router.urls

urlpatterns = patterns('',
    #url(r'^$', 'django.views.defaults.page_not_found', name='api-main'),
    #url(r'^$', 'django.views.defaults.server_error', name='api-main'),
    #url(r'^$', 'django.views.defaults.bad_request', name='api-main'),
    #url(r'^$', 'django.views.defaults.permission_denied', name='api-main'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inventory/$', views.InventoryList.as_view(), name='inventory-list'),
    url(r'^inventory/(?P<pk>[-\w]+)$', views.InventoryDetail.as_view(), name='inventory-detail'),
    url(r'^merchants/$', views.MerchantList.as_view(), name='merchant-list'),
    url(r'^merchants/(?P<pk>[-\w]+)$', views.MerchantDetail.as_view(), name='merchant-detail'),
    url(r'^wallets/$', views.WalletList.as_view(), name='wallet-list'),
    url(r'^wallets/(?P<pk>\d+)$', views.WalletDetail.as_view(), name='wallet-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\d+)$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^', include('rest_framework.urls', namespace='rest_framework'))
)
urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    