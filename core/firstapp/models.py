from django.db import models

class userModel(models.Model):
    name = models.CharField(max_length = 100)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length = 11)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"Name: {self.name}, PhoneNumber: {self.phone}"


