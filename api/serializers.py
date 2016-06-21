from rest_framework import serializers
from frontend.models import *


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id',
                  'name',
                  'birthday',
                  'bio',
                  'picture',
                  'phone')