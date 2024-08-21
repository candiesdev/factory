from django.shortcuts import render

# Create your views here.

def index(request):
  if not request.user.is_authenticated:
<<<<<<< HEAD
    session = False
    user = ''
  else:
    session = True
    user = request.user
  return render(request, "home/index.html", { 'session': session, 'user': user})
=======
    session = True
  else:
    session = False
  return render(request, "home/index.html", {'session': session})
>>>>>>> b36bfaf5e32d080c5fa931062a6a565011dc310b
