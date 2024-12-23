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
    path('start_reg/', views.start_reg)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    