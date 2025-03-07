from rest_framework import serializers
from ecomapp import models
from .models import *


class userserializer(serializers.ModelSerializer):
    class Meta:
        model = register
        fields = '__all__'

      