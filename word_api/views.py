from rest_framework import generics
from word.models import Word
from .serializers import WordSerializer

class WordList(generics.ListAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

class WordDetail(generics.RetrieveAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer