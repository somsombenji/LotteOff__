from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('shop/', include('shop.urls', namespace='shop')),
    path('cart/', include('cart.urls')),
    path('', include('chatApp.urls')),
    path('', include('driveApp.urls')),
    path('', include('newProduct.urls')),
    path('', include('selectApp.urls')),
    path('accounts/', include('allauth.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
