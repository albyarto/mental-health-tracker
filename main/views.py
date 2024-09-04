from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306241695',
        'name': 'Muhammad Albyarto Ghazali',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)