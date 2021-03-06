from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from friendship.models import Friend, Follow
from sorl.thumbnail import delete
from accounts.forms import TerminationForm
from pet.forms import EmailForm
from pet.models import Person, Board, Picture


def forgot_password(request):
    if request.method == 'POST':
        return password_reset(request, from_email=request.POST.get('email'))
    return render(request, 'forgot_password.html')


@login_required
def change_email(request):
    form = EmailForm(request)
    if request.method == "POST":
        form = EmailForm(request, request.POST)
        if form.is_valid():
            user = Person.objects.get(username=request.user)
            email = form.cleaned_data['email']
            user.email = email
            user.save()
            return HttpResponseRedirect(reverse('world:profile', kwargs={'username': user.slug}))

    return render(request, 'email.html', {'form': form})


@login_required
def termination(request):
    form = TerminationForm()
    if request.method == "POST":
        form = TerminationForm(request.POST)
        if form.is_valid():
            person = Person.objects.get(username=request.user)
            board = Board.objects.filter(user=request.user)
            picture = Picture.objects.filter(board=board)
            for p in picture:
                delete(p.image)
                p.delete()
            for b in board:
                b.delete()
            friend = Friend.objects.friends(person)
            for f in friend:
                Friend.objects.remove_friend(person, f)
            following = Follow.objects.following(request.user)
            for f in following:
                Follow.objects.remove_follower(person, f)
            for f in following:
                Follow.objects.remove_follower(person, f)
            requests = Friend.objects.unread_requests(user=request.user)
            for f in requests:
                f.delete()
            person.is_active = False
            person.email = None
            person.date_of_birth = None
            person.image.delete()
            person.save()
            return HttpResponseRedirect(reverse('world:logout_request'))
    return render(request, 'termination.html', {'form': form})
