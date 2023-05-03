from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.save(update_fields=['email', 'username', 'first_name'])
        return instance

    class Meta:
        model = User
        fields = '__all__'
