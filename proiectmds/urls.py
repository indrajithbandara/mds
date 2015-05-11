from django.conf.urls import include, url
from django.contrib import admin

from teme import views
from . import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
]