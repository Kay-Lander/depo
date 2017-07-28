from django.shortcuts import render, redirect, reverse
from ..login.models import User



# Create your views here.
def currentUser( request):
    id = request.session['user_id']

    return User.objects.get(id=id)

def index(request):
    if 'user_id' in request.session:
        first_user = currentUser(request)

        friends = first_user.friends.all()

        users = User.objects.exclude(id__in=friends).exclude(id=first_user.id)

    context = {
        'users': users,
        'friends': friends,
        'first_user': first_user,
    }
    return render(request, 'belt/index.html', context)

def add(request, id):
    if request.method == "POST":
        if 'user_id' in request.session:
            first_user = currentUser(request)
            want_user = User.objects.get(id=id)

            first_user.friends.add(want_user)

        return redirect(reverse('success'))

def show(request, id):
    first_user = currentUser(request)
    view_user = User.objects.get(id=id)
    their_user = view_user.friends.all().first()

    context = {
        'view_user':view_user,
        'their_user':their_user,
    }
    return render(request, 'belt/display.html', context)

def remove(request, id):
        if request.method == "POST":
            if 'user_id' in request.session:
                first_user = currentUser(request)
                want_user = User.objects.get(id=id)

                first_user.friends.remove(want_user)

            return redirect(reverse('success'))
