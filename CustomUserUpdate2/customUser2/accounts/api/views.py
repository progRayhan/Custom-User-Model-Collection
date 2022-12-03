from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import CustomUser
from accounts.api.serializers import CustomUserSerializer

class RegistrationAV(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = 'Registration Successfully'
            data['email'] = account.email
            data['username'] = account.username
            data['phone'] = account.phone
            return Response(data)

        else:
            return Response(serializer.errors)
