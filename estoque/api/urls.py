from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, StockMovementViewSet, CustomAuthToken

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'movements', StockMovementViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', CustomAuthToken.as_view(), name='api_token_auth'),
]
