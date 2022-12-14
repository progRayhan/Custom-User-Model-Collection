from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import Profile
from accounts.api.serializers import ProfileSerializer
from rest_framework import status

class ProfileListAV(APIView):
    def get(self, request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class ProfileDetailsAV(APIView):
    def get(self, request, pk):
        profile = Profile.objects.get(pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    # def put(self, request, pk):
    #     profile = Profile.objects.get(pk=pk)
    #     serializer = ProfileSerializer(profile, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_200_OK)
