from accounts.models import Account
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('email','username','password','first_name')
        extra_kwargs = {'password':{'write_only':True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        user = self.Meta.model(**validated_data)

        if not password:
            raise ValidationError("Password is required for registration.")

        user.set_password(password)
        user.save()
        return user


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields=('email','username','first_name')
