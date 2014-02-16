from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from cms.sitemaps import CMSSitemap

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jsite.views.home', name='home'),
    # url(r'^jsite/', include('jsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls')), 
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^', include('cms.urls')),

)

# urlpatterns += patterns('',
#                 url(r'^polls/', include('polls.urls')), 
# )

if settings.DEBUG:
    urlpatterns = patterns('',
        # 
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
        
    ) + urlpatterns
