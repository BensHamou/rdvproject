from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('rdv/admin/', admin.site.urls),
    path("", include('rdv.urls')),
]
