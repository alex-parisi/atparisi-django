from django.contrib import admin
from django.urls import path, include, re_path
from .views import home
from django.views.static import serve
import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("projects/", include("projects.urls")),
    path('', home, name='home'),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]