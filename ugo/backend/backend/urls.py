from django.conf.urls import url
from django.urls import include

urlpatterns = [    
    url(r'api/', include('app.authorization.urls')),
    url(r'api/', include('app.product.urls')),
    url(r'api-auth/', include('rest_framework.urls'))
]
