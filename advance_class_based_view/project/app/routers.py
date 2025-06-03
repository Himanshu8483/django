from rest_framework import routers
from .views import StudentViewSet
router = routers.SimpleRouter()
router.register(r'student', StudentViewSet, basename='student')
# urlpatterns = router.urls