from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from .models import UserProfile
from .permissions import UpdateOwnProfile
from .serializers import UserProfileSerializer


# Create your views here.
class UserProfileViewSet(ModelViewSet):

	serializer_class = UserProfileSerializer
	queryset = UserProfile.objects.all()
	permission_classes = (UpdateOwnProfile, )
	filter_backends = (SearchFilter, )
	search_fields = ('id', 'email', 'first_name')
