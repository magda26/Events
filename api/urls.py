from rest_framework import routers

from api.views import EventViewSet

router = routers.DefaultRouter()
router.register('events', EventViewSet)
