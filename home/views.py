from django.shortcuts import render

# Create your views here.
def coming_soom(request):
    return render(request, 'coming_soon.html')