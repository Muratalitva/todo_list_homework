from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'created_at', 'age']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=100, write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=100, write_only=True
    )

    class Meta:
        model = User 
        fields = ('username', 'password', 'confirm_password', 'phone')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':'Пароли отличаются'})
        elif attrs['phone'][:4] != "+996" or len(attrs['phone']) > 13:
            raise serializers.ValidationError({'phone':'Неправильный формат номера (+996)'})
        return attrs
