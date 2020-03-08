from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('eventsManager/', include('eventsManager.urls')),
    path('admin/', admin.site.urls),
]