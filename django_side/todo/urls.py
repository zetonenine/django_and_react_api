from rest_framework import routers
from .api import ToDoViewSet

router = routers.DefaultRouter()
router.register('api/todo', ToDoViewSet, 'todo')

urlpatterns = router.urls
