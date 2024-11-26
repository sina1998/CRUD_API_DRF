from rest_framework import serializers

class profileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    phone = serializers.IntegerField()
    age = serializers.IntegerField()
    email = serializers.EmailField()

    def __str__(self) -> str:
        return self.name

class profile(object):
    def __init__(self, name, phone, age, email):
        self.name = name
        self.phone = phone
        self.age = age
        self.email = email

