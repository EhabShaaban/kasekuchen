from rest_framework import generics
from word.models import Word
from .serializers import WordSerializer

class WordList(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

class WordDetail(generics.RetrieveDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer