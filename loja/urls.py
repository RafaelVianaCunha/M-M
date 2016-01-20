from django.conf.urls import patterns, include, url
from loja import views
from django.contrib import admin


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'connectedin.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),


                       url(r'^$', views.index, name='index'),
                       url(r'^produto/$', views.produto, name='produto'),
                       url(r'^pagamento/$', views.pagamento, name='pagamento'),
                       )
