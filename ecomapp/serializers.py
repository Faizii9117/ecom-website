from rest_framework import serializers
from ecomapp import models
from .models import *


class userserializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'

      