from rest_framework import serializers
from .models import User

class User_Serializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User 
        fields = ['id','name','phone_no','email','password']
        extra_kwargs={
            'password':{'write_only':True},
            'id':{'read_only':True},
        }

        def create(self,validated_data):
            user = User.objects.create.usser(
                phone_no=validated_data['phone_no'],
                password=validated_data['password'],
                name=validated_data['name'],
                email=validated_data['email',''],
            )
            return user 