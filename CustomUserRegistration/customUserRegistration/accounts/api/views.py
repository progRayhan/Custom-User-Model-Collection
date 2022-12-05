import random
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import CustomUser
from accounts.api.serializers import CustomUserSerializer

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

            data = {}
            data['response'] = 'Registration Sucessfully'
            data['email'] = account.email
            data['username'] = account.username
            data['phone'] = account.phone
            data['verify_code'] = account.verify_code
            return Response(data)
        
        else:
            return Response(serializer.errors)
