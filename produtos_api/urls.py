from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^produtos/$', views.ProdutosList.as_view()),
    url(r'^produto/(?P<pk>[0-9]+)/$', views.ProdutosListDetails.as_view()),
    url(r'^fornecedores/$', views.FornecedoresList.as_view()),
    url(r'^fornecedor/(?P<pk>[0-9]+)/$', views.FornecedoresListDetails.as_view()),
]