from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^media/(?P<path>.*)$', serve, {'document_root':
    #                                              settings.MEDIA_ROOT}),  # serve media files when deployed
    # re_path(r'^static/(?P<path>.*)$', serve, {'document_root':
    #                                               settings.STATIC_ROOT}),  # serve static files when deployed
    path('', include('ticketing.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('register.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
