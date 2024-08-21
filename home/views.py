from django.shortcuts import render

# Create your views here.

def index(request):
  if not request.user.is_authenticated:
    session = False
    user = ''
  else:
    session = True
    user = request.user
  return render(request, "home/index.html", { 'session': session, 'user': user})