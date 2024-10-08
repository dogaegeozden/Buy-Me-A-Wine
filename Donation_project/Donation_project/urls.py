# LIBRARIES
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

# URL PATTERS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wine_store.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG == True:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
