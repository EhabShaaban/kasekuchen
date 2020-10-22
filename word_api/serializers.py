from rest_framework import serializers
from word.models import Word

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('string' , 'length' , 'language' , 'data_posted')