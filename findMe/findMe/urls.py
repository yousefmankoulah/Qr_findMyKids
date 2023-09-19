from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [

]
    
urlpatterns += i18n_patterns(
    path(_('findmeAdmin/'), admin.site.urls),
    path('', include('home.urls')),
    path('product/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('customer_service/', include('customer_service.urls')),
    path('rosetta/', include('rosetta.urls')),
)



###############################################

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)