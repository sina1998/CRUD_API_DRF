from rest_framework import serializers
from firstapp.models import userModel

class userSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = userModel
        fields = "__all__"
    
class createUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = userModel
        fields = ["name", "age", "phone", "email"]