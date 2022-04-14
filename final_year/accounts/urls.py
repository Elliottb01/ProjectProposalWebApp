from unicodedata import name
from django.urls import URLPattern, path
from . import views
from .views import edit_profile_page, show_profile_page
from django.conf import settings
from django.conf.urls.static import static


app_name = 'accounts'

urlpatterns = [

    path('signup/', views.signup_view, name="signup" ),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('<int:pk>/profile/', show_profile_page.as_view(), name="show_profile"),
    path('<int:pk>/profile/edit/', edit_profile_page.as_view(), name="edit_profile" ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)