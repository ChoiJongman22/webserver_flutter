from rest_framework import serializers
from .models import Webrtc

class WebRtcSerializer(serializers.ModelSerializer):
    class Meta:
        model=Webrtc
        fields=('title','body','answer')