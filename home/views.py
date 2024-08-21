from django.shortcuts import render

# Create your views here.

def index(request):
  if not request.user.is_authenticated:
    session = True
  else:
    session = False
  return render(request, "home/index.html", {'session': session})