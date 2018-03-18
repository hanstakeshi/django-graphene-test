from django.conf.urls import url
from django.contrib import admin
from filebrowser.sites import site
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from apps.web import urls as web_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Filebrowser url
    url(r'^admin/filebrowser/', include(site.urls)),
    # Application number 1
    url(r'', include(web_urls, namespace='web')),
    # Add Anothers applications
] + (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
