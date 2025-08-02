from django.urls import path
from .views import user_login, user_register
from django.conf import settings
from django.conf.urls.static import static

# from .views import valides_annonces

urlpatterns = [
    path('login/', user_login),
    path('register/', user_register),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)