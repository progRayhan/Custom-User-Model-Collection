import random
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import CustomUser
from accounts.api.serializers import CustomUserSerializer

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

class RegistrationAV(APIView):
    def post(self, request):

        # convert immutable data to muutable data
        myVariable = request.data
        myVariable._mutable = True

        # generate random number
        randomNumber = str(random.randint(100000, 999999))

        # push random code to "verify_code" field
        myVariable['verify_code'] = randomNumber

        serializer = CustomUserSerializer(data=myVariable)
        if serializer.is_valid():
            account = serializer.save()

            # For Email Sending (Start)
            message = render_to_string('account.html',{
                'user':"account",
                'domain':"current_site.domain",
                "verify_code" : request.data['verify_code']
            })

            subject, from_email, to = 'hey', 'rayhan.bdappdeveloper@gmail.com', request.data['email']
            text_content = 'Your Account Information'
            msg = EmailMultiAlternatives(subject, from_email,text_content, [to])
            msg.attach_alternative(message, "text/html")
            
            if msg.send() == True:
            # For Email Sending (End)

                data = {}
                data['response'] = 'Registration Sucessfully'
                data['email'] = account.email
                data['username'] = account.username
                data['phone'] = account.phone
                data['verify_code'] = account.verify_code
                return Response(data)
        
        else:
            return Response(serializer.errors)
