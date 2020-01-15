from rest_framework import serializers
from django_enum_choices.serializers import EnumChoiceModelSerializerMixin
from .models import post

# Serializer for post model
class postSerializer(EnumChoiceModelSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ('id', 'title', 'body', 'status', 'created_on')
        extra_kwargs = {'author': {'read_only': True}}