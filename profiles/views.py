from django.shortcuts import render
from rest_framework import filters
from rest_framework.generics import ListAPIView

from profiles.models import Profile
from profiles.serializers import ProfileSerializer


class ProfilesList(ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('prefered_location', 'current_location', 'skills', 'work_experience')
