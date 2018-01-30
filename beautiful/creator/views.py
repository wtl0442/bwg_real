from django.shortcuts import render

# Create your views here.
def creator_main(request):
    return render(request, 'creator/creator_main.html')