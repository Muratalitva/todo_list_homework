from rest_framework.routers import DefaultRouter

from users.views import UserAPIViewSet

router = DefaultRouter()
router.register('users', UserAPIViewSet, 'api_users')

urlpatterns = router.urls