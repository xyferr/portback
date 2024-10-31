from django.shortcuts import render
from .serializers import MessagesSerializer
from rest_framework.response import Response
from .models import Messages
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.

@api_view()
@permission_classes([IsAuthenticated])
def get_messages(request):
    list = Messages.objects.all()
    serializer = MessagesSerializer(list,many=True)
    return Response(
        {
            'data':serializer.data
            # 'data':'Hello Rohit'
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
        try:
            name_from_customer = serializer.validated_data.get('name')
            email_from_customer = serializer.validated_data.get('email')
            email_subject = f"Hi {name_from_customer}, It's Rohit"
            email_body = "Thank You for contacting us. We will get back to you soon. You contact me on linkedin for more information"
            email = EmailMessage(
                email_subject,
                email_body,
                "ROHIT <star080war@gmail.com>",
                [email_from_customer],
            )
            email.send(fail_silently=False)
            messages.success(request,'Email sent successfully')
            print("Email sent successfully")
        
        except Exception as e:
            messages.warning(request,'Unable to send email')
            print(e)
        return Response(
            {
                'message':"Message sent successfully"
            }
        )
   
    
    