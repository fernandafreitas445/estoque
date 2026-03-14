from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField("Nome", max_length=100)
    description = models.TextField("Descrição", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Product(models.Model):
    name = models.CharField("Nome do Produto", max_length=150)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products", verbose_name="Categoria")
    description = models.TextField("Descrição", blank=True, null=True)
    price = models.DecimalField("Preço", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("Quantidade em Estoque", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"


class StockMovement(models.Model):
    MOVEMENT_TYPES = (
        ('IN', 'Entrada'),
        ('OUT', 'Saída'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="movements", verbose_name="Produto")
    movement_type = models.CharField("Tipo de Movimentação", max_length=3, choices=MOVEMENT_TYPES)
    quantity = models.PositiveIntegerField("Quantidade")
    date = models.DateTimeField("Data", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Usuário")

    def __str__(self):
        return f"{self.get_movement_type_display()} - {self.product.name} ({self.quantity})"

    class Meta:
        verbose_name = "Movimentação de Estoque"
        verbose_name_plural = "Movimentações de Estoque"
