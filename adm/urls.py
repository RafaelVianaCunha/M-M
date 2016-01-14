from django.conf.urls import patterns, include, url
from adm import views
from django.contrib import admin
from views import CadastrarProduto

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'connectedin.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^adm/$', views.adm, name='adm'),
                       url(r'^cadastrarProduto/$', CadastrarProduto.as_view(), name='cadastrarProduto'),
                       )
