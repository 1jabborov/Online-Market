from rest_framework import serializers
from .models import Client

# Enter your serializers here.


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = "id", "full_name", "phone", "balance"
