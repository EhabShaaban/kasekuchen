from django.urls import path
from .views import WordList, WordDetail

app_name = 'word_api'

urlpatterns = [
    path('', WordList.as_view(), name= 'listcreate'),
    path('<int:pk>/', WordDetail.as_view(), name= 'detailcreate'),
]