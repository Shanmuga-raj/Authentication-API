from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserProfile
		fields = ('id', 'email', 'first_name', 'last_name', 'date_of_birth', 'profile_picture', 'password')
		extra_kwargs = {
			'password': {
				'write_only': True,
				'style': {
					'input_type': 'password'
				}
			}
		}

	def create(self, validated_data):
		"""Create and return a new user"""
		user = UserProfile.objects.create_user(
			email=validated_data['email'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name'],
			date_of_birth=validated_data['date_of_birth'],
			profile_picture=validated_data['profile_picture'],
			password=validated_data['password']
		)

		return user

	def update(self, instance, validated_data):
		"""Handle updating user account"""
		if 'password' in validated_data:
			password = validated_data.pop('password')
			instance.set_password(password)

		return super().update(instance, validated_data)
