from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.upload_photo, name='upload_photo'),
    path('photos/', views.photo_list, name='photo_list'),
      path('delete_all_photos/', views.delete_all_photos, name='delete_all_photos'),
]
# Configuration pour servir les fichiers médias en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)