from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from profiles.api.serializers import ProfileSerializer
from profiles.models import Profile


class ProfileList(generics.ListAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
