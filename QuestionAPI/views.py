from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer 
from rest_framework.response import Response
from Question.models import Questions
# Create your views here.
@api_view(['GET'])
def index(request):
    if request.method =='GET':
        question=Questions.objects.all()
        serializer= QuestionSerializer(question,many=True)
        return Response(serializer.data)

