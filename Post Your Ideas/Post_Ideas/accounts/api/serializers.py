from rest_framework import serializers
from accounts.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = Profile
        fields = ['email', 'first_name', 'last_name', 'phone', 'password', 'password2']

        extra_kwargs = {
            'password' : {
                'write_only': True,
            }
        }

    def save(self):
        customProfile = Profile(
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            phone = self.validated_data['phone'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'password must be match'})

        customProfile.set_password(password)
        customProfile.save()
        return customProfile