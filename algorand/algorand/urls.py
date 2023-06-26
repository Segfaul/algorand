from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from algorand import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('algos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'algos.views.tr_handler403'
handler404 = 'algos.views.tr_handler404'
handler500 = 'algos.views.tr_handler500'
