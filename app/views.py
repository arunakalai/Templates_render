from django.shortcuts import render


# Create your views here.
def Html(request):
    return render(request,'sample.html')
