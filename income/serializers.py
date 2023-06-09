from rest_framework import serializers
from .models import Income, IncomeItem

# Create your serializers here.


class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = "__all__"


class IncomeItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = IncomeItem
        fields = "__all__"
