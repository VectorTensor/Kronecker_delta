from rest_framework import serializers
from Question.models import Questions
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('Question','Answer')
        model= Questions


