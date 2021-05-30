from rest_framework import serializers
from messenger.models import Messages

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('Message','User')
        model=Messages
