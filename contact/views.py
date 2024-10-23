from django.shortcuts import render
from .serializers import MessagesSerializer
from rest_framework.response import Response
from .models import Messages
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import HttpResponse

# Create your views here.

@api_view()
def get_messages(request):
    list = Messages.objects.all()
    serializer = MessagesSerializer(list,many=True)
    return Response(
        {
            'data':serializer.data
        }
    )
    
def home(request):
    return HttpResponse("Working Good ROHIT , You are the best")

class MessageAPI(APIView):
    def get(self,request):
        
        return Response(
            {
                'message':"This is get request"
            }
        )
    
    def post(self,request):
        data = request.data
        serializer = MessagesSerializer(data=data)
        if not serializer.is_valid():
            return Response(
                {
                    'error':serializer.errors
                }
            )
        serializer.save()
        return Response(
            {
                'message':"Message sent successfully"
            }
        )
   
    
    