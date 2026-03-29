from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from menu import views as menu_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu_views.home, name='home'),
    path('menu/', menu_views.menu, name='menu'),
    path('about/', menu_views.about, name='about'),
    path('contact/', menu_views.contact, name='contact'),
    path('product/<int:pk>/', menu_views.product_detail, name='product_detail'),
    path('cart/', menu_views.cart, name='cart'),
    path('cart/add/<int:pk>/', menu_views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', menu_views.remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', menu_views.clear_cart, name='clear_cart'),
    path('order/confirm/', menu_views.order_confirm, name='order_confirm'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
