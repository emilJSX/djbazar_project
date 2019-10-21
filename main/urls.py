from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path,include
from django.conf.urls.i18n import i18n_patterns


urlpatterns = i18n_patterns( 
   
    path('admin/', admin.site.urls),
    path('',include('djstore.urls',namespace='djstore')),
    re_path(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    re_path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    
   
)


urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)