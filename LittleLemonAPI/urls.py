from django.urls import path
from .views import CategoryListCreateView, CategoryRetrieveUpdateDeleteView, MenuItemListCreateView,MenuItemRetrieveUpdateDeleteView,CartListCreateView, CartRetrieveUpdateDeleteView,OrderListCreateView,OrderRetrieveUpdateDeleteView,OrderItemListCreateView,OrderItemRetrieveUpdateDeleteView,UserListCreateView,UserRetrieveUpdateDeleteView

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDeleteView.as_view(), name='category-detail'),

    # MenuItem URLs
    path('menuitems/', MenuItemListCreateView.as_view(), name='menuitem-list'),
    path('menuitems/<int:pk>/', MenuItemRetrieveUpdateDeleteView.as_view(), name='menuitem-detail'),
    
     # Cart URLs
    path('carts/', CartListCreateView.as_view(), name='cart-list'),
    path('carts/<int:pk>/', CartRetrieveUpdateDeleteView.as_view(), name='cart-detail'),

    # Order URLs
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDeleteView.as_view(), name='order-detail'),

    # OrderItem URLs
    path('orderitems/', OrderItemListCreateView.as_view(), name='orderitem-list'),
    path('orderitems/<int:pk>/', OrderItemRetrieveUpdateDeleteView.as_view(), name='orderitem-detail'),
    
     # User URLs
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDeleteView.as_view(), name='user-detail'),
]

