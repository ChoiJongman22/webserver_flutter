from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Webrtc
from .serializers import WebRtcSerializer
import random

@api_view(['GET'])
def randomWebrtc(request,id):
    totalwebrtc=Webrtc.objects.all()
    randomWebrtc = random.sample(list[totalwebrtc],id)
    serailizer=WebRtcSerializer(randomWebrtc,many=True)
    return Response(serailizer.data)
