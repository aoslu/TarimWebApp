from django.shortcuts import render

def anasayfa(request):
    return render(request,"ev/anasayfa.html")