from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated 
from users.permissions import IsOwnerOrReadOnly
from users.utils import get_tokens_for_user

from apps.todo.models import Task
from apps.todo.serializers import ToDoSerializer

# Create your views here.
class ToDoAPIViewSet(GenericViewSet,
                     ListModelMixin,
                     RetrieveModelMixin, 
                     CreateModelMixin, 
                     UpdateModelMixin, 
                     DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

