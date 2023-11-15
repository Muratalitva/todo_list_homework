from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated 
from users.permissions import IsOwnerOrReadOnly 
from users.utils import get_tokens_for_user

from users.models import User
from users.serializers import UserSerializer

# Create your views here.
class UserAPIViewSet(GenericViewSet,
                     ListModelMixin,
                     RetrieveModelMixin, 
                     CreateModelMixin, 
                     UpdateModelMixin, 
                     DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]