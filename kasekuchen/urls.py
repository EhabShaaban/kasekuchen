from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('word.urls', namespace='word')),
    path('api/', include('word_api.urls', namespace='word_api')),
]
