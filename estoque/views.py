from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.contrib import messages

from .models import Category, Product, StockMovement
from .forms import CategoryForm, ProductForm, StockMovementForm

# --- PRODUCT VIEWS ---
class ProductListView(ListView):
    model = Product
    template_name = 'estoque/product_list.html'
    context_object_name = 'products'
    # No LoginRequiredMixin - public list as per requirements

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'estoque/product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        messages.success(self.request, "Produto criado com sucesso.")
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'estoque/product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        messages.success(self.request, "Produto atualizado com sucesso.")
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'estoque/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Produto deletado com sucesso.")
        return super().delete(request, *args, **kwargs)

# --- CATEGORY VIEWS ---
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'estoque/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'estoque/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'estoque/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'estoque/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

# --- STOCK MOVEMENT VIEWS ---
class StockMovementListView(LoginRequiredMixin, ListView):
    model = StockMovement
    template_name = 'estoque/movement_list.html'
    context_object_name = 'movements'

class StockMovementCreateView(LoginRequiredMixin, CreateView):
    model = StockMovement
    form_class = StockMovementForm
    template_name = 'estoque/movement_form.html'
    success_url = reverse_lazy('movement_list')

    def form_valid(self, form):
        with transaction.atomic():
            movement = form.save(commit=False)
            movement.user = self.request.user
            
            product = movement.product
            if movement.movement_type == 'IN':
                product.quantity += movement.quantity
            elif movement.movement_type == 'OUT':
                if product.quantity < movement.quantity:
                    form.add_error('quantity', 'Quantidade em estoque insuficiente.')
                    return self.form_invalid(form)
                product.quantity -= movement.quantity
            
            product.save()
            movement.save()
            messages.success(self.request, "Movimentação registrada com sucesso.")
        return super().form_valid(form)
