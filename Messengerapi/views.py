from django.shortcuts import render
from messenger.models import Messages 
from rest_framework.decorators import api_view
from .serializers import MessagesSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def index(request):
    if request.method =='GET':
        message=Messages.objects.all()
        serializer=MessagesSerializer(message,many=True)
        return Response(serializer.data)
