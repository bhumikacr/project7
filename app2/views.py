from django.shortcuts import render

# Create your views here.
def tajmahal(request):
    return render(request,'taj mahal.html')
def charminar(request):
    return render(request,'charminar.html')

