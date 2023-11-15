from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

def get_tokens_for_user(user): 
    refresh = RefreshToken.for_user(user)
    return { 'refresh': str(refresh), 'access': str(refresh.access_token), }

