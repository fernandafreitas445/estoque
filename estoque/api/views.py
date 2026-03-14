from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction

from estoque.models import Category, Product, StockMovement
from .serializers import CategorySerializer, ProductSerializer, StockMovementSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class StockMovementViewSet(viewsets.ModelViewSet):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        with transaction.atomic():
            movement = serializer.save(user=request.user if request.user.is_authenticated else None)
            product = movement.product
            
            if movement.movement_type == 'IN':
                product.quantity += movement.quantity
            elif movement.movement_type == 'OUT':
                if product.quantity < movement.quantity:
                    transaction.set_rollback(True)
                    return Response({'error': 'Quantidade em estoque insuficiente.'}, status=status.HTTP_400_BAD_REQUEST)
                product.quantity -= movement.quantity
            
            product.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
