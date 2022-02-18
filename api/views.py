from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.settings import api_settings
from .models import UserProfile
from .permissions import UpdateOwnProfile
from .serializers import UserProfileSerializer


# Create your views here.
class UserProfileViewSet(ModelViewSet):
	"""API to Get, Put, Patch, Delete. (CRUD)"""
	serializer_class = UserProfileSerializer
	queryset = UserProfile.objects.all()
	authentication_classes = (TokenAuthentication, )
	permission_classes = (UpdateOwnProfile, )
	filter_backends = (SearchFilter, )
	search_fields = ('id', 'email', 'first_name')


class UserLoginApiView(ObtainAuthToken):
	"""Login API to generate a Token."""
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
