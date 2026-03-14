from rest_framework import serializers
from estoque.models import Category, Product, StockMovement

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class StockMovementSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = StockMovement
        fields = '__all__'
        read_only_fields = ['date', 'user']
