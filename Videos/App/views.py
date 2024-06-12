from django.shortcuts import render
from App.serializers import LessonSerializers
from .models import Lesson
from rest_framework import viewsets, generics,permissions
# Create your views here.
class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializers
    permission_classes = [permissions.DjangoModelPermissions]


    def get_queryset(self):
        return Lesson.objects.all()