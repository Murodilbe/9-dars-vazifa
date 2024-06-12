from .models import Lesson
from rest_framework import serializers
from .models import Lesson
class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
