
from nturl2path import pathname2url
from unicodedata import name
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from projects import views as project_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include ('projects.urls')),
    path('about/', views.about, name="about-page"),
    path('projects/', project_views.project_list.as_view(), name="home"),
    path('accounts/', include ('accounts.urls')),
    path('', views.homepage, name="homepage"),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)