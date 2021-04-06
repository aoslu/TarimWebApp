from django.urls import path
from hakkitarim.views import anasayfa
urlpatterns = [
    path('',anasayfa, name="anasayfa"),
]
