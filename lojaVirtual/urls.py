from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lojaVirtual.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
                       url(r'^', include('adm.urls')),
                       url(r'^', include('loja.urls')),

)
