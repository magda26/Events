
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from api.urls import router as events_router
from rest_auth.views import LoginView
from api import views

router = routers.DefaultRouter()
router.registry.extend(events_router.registry)

urlpatterns = [
    path('', views.index ),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/api-auth/',LoginView.as_view()),
    path('api/create-user/', include('rest_auth.registration.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
