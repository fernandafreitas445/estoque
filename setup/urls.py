from django.urls import path, include

urlpatterns = [
    path('', include('estoque.urls')),
    path('api/', include('estoque.api.urls')),
]
