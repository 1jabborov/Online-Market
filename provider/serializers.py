from rest_framework import serializers
from .models import Provider

# Enter your serializers here.


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = "__all__"
