# myapp/urls.py

from rest_framework.routers import DefaultRouter
from .views import MyModelViewSet, UsersView

router = DefaultRouter()
router.register(r'mymodel', MyModelViewSet, basename='mymodel')
router.register(r'users', UsersView, basename="users")
urlpatterns = router.urls
