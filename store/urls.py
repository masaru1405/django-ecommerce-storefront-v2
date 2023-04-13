from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

carts_routers = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_routers.register('items', views.CartItemViewSet, basename='cart-items')

#URLConf
urlpatterns = router.urls + products_router.urls + carts_routers.urls

# urlpatterns = [
#    path('products/', views.ProductList.as_view()),
#    path('products/<int:pk>/', views.ProductDetail.as_view()),
#    path('collections/', views.CollectionList.as_view()),
#    path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail')
# ]