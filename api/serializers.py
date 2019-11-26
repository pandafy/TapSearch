from rest_framework import serializers
from .models import *


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ("id", "text")


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = ("word",)


class WordFrequenciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = WordFrequencies
        fields = ("id", "frequency", "doc_id",)
