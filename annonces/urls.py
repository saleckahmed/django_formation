
from django.urls import path
from .views import annonces, add_category, add_annonce
from django.conf import settings
from django.conf.urls.static import static

# from .views import valides_annonces

urlpatterns = [
    # path('valides_annonces/', valides_annonces),
    path('', annonces),
    path('add-category/', add_category),
    path('add-annonce/', add_annonce),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)