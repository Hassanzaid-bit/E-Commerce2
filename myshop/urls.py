
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/', include('payment.urls', namespace='payment')),
    path('api/v1/', include('mpesa_api.urls')),
    path('home/', include('computers.urls', namespace='computers')),
    path('components/', include('components.urls', namespace = 'components')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('account/', include('account.urls', namespace='account')),
  
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
