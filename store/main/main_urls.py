from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('search/', views.search),
    path('search_mini', views.search_mini),
    path('product/<int:id>', views.product),
    path('start_login/', views.start_login),
    path('logout/', views.profile_logout),
    path('start_reg/', views.start_reg),
    path('profile/', views.profile),
    path('change_profile', views.change_profile),
    path('create_shop', views.create_shop),
    path('update/<int:id>', views.update),
    path('add_products/<int:id>', views.add_products),
    path('add_product/<int:id>', views.add_product),
    path('del_product/', views.del_product),
    path('update_product/<int:id>', views.update_product),
    path('catalog/<int:id>', views.catalog),
    path('cart/', views.cart),
    path('add_cart/', views.add_cart)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    