from django.urls import include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from app.product import views

urlpatterns = [    
    url(r'api/', include('app.authorization.urls')),
    url(r'api/', include('app.product.urls')),

    url(r'api-auth/', include('rest_framework.urls'))
]
 
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)