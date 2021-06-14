from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, 'index.html')

def viewPage(request):
    return render(request, 'view.html')    