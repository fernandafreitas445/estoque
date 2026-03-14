from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Public page
    path('', views.ProductListView.as_view(), name='product_list'),
    
    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='estoque/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # Product CRUD (Protected)
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    
    # Category CRUD (Protected)
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # Stock Movement CRUD (Protected)
    path('movement/', views.StockMovementListView.as_view(), name='movement_list'),
    path('movement/create/', views.StockMovementCreateView.as_view(), name='movement_create'),
]
