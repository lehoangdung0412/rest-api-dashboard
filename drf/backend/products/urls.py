from django.urls import URLPattern, path

from . import views

# /api/products/
urlpatterns = [
    path('', views.product_mixin_list_view),
    path('<int:pk>/update/', views.product_mixin_detail_view),
    path('<int:pk>/delete/', views.product_mixin_detail_view),
    path('<int:pk>/', views.product_mixin_detail_view)
]
