from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model
class TaskSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True, default='description',)
    image = serializers.ImageField(max_length=None, use_url=True)
    doc = serializers.FileField(max_length=None, use_url=True)



    class Meta:
        model = Task
        fields = ('user', 'task_name', 'task_desc', 'completed', 'date', 'image', 'doc',)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')