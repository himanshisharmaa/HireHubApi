from django.shortcuts import render
from rest_framework import generics,permissions,filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Job
from .serializers import JobSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class JobListCreateView(generics.ListCreateAPIView):
    queryset=Job.objects.all()
    serializer_class=JobSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['location', 'company_name']   # Fields you want to allow filtering on
    search_fields = ['title', 'description', 'company_name']

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class JobRetrieveUpdateDestroyView(generics.RetrieveUpdateAPIView):
    queryset=Job.objects.all()
    serializer_class=JobSerializer
    permission_classes=[IsOwnerOrReadOnly]