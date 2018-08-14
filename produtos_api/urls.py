from produtos_api.views import ProdutoViewSet,FornecedorViewSet,GerarAuthToken
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet, base_name='produto')
router.register(r'fornecedores', FornecedorViewSet, base_name='fornecedor')
urlpatterns = router.urls