from rest_framework import serializers
from accounts.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'phone', 'fvrtColor','verify_code', 'password', 'password2']

        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def save(self):
        customUser = CustomUser(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            phone = self.validated_data['phone'],
            fvrtColor = self.validated_data['fvrtColor'],
            verify_code = self.validated_data['verify_code'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'password must be match'})

        customUser.set_password(password)
        customUser.save()
        return customUser