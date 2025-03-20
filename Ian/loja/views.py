from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Cliente, Produto, Venda, ItemDaVenda 
from .serializers import ClienteSerializer, ProdutoSerializer, VendaSerializer, ItemDaVendaSerializer 

class ClienteViewSet(viewsets.ModelViewSet): 
    queryset = Cliente.objects.all() 
    serializer_class = ClienteSerializer 
    permission_classes = [permissions.IsAuthenticated] 

class ProdutoPagination(PageNumberPagination):
    page_size = 10 #degine 10 produtos por pagina
    page_size_query_param = 'page_size' #permite definir um tamanho diferente via query param
    max_page_size = 100 #limita o máximo de produtos dpor pagina
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all() 
    serializer_class = ProdutoSerializer 
    pagination_class = ProdutoPagination # adiciona paginção personalizada
    def get_permissions(self): 
        if self.action in ['create', 'update', 'partial_update', 'destroy']: 
            return [permissions.IsAdminUser()] 
        return [permissions.AllowAny()] 
class VendaViewSet(viewsets.ModelViewSet): 
    queryset = Venda.objects.all() 
    serializer_class = VendaSerializer 
    permission_classes = [permissions.IsAuthenticated] 
class ItemDaVendaViewSet(viewsets.ModelViewSet): 
    queryset = ItemDaVenda.objects.all() 
    serializer_class = ItemDaVendaSerializer 
    permission_classes = [permissions.IsAuthenticated]