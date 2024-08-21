from django.shortcuts import render

# Create your views here.

def index(request):
  user = ''
  if not request.user.is_authenticated:
    session = False
  else:
    session = True
    user = request.user
  return render(request, "home/index.html", {'session': session, 'user_name': user})