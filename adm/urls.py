from django.conf.urls import patterns, include, url
from adm import views
from django.contrib import admin
from views import CadastrarProduto, CategoriaView, SubCategoriaView

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'connectedin.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^adm/index$', CadastrarProduto.as_view(), name='adm'),
                       url(r'^adm/base$', views.base, name='baseAdmin'),
                       url(r'^adm/produto', CadastrarProduto.as_view(), name='produto'),
                       url(r'^adm/subcategoria', SubCategoriaView.as_view(), name='subcategoria'),
                       url(r'^adm/categoria', CategoriaView.as_view(), name='categoria'),
                       url(r'^cadastrarProduto/$', CadastrarProduto.as_view(), name='cadastrarProduto'),
                       )
