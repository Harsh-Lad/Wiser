from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as loginFunc, logout
from django.contrib.auth.models import User
# import messages
from django.contrib import messages
from .models import *
from .forms import jounralForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        mood = request.POST['mood']
        user = request.user
        mood = Mood.objects.create(user=user, mood=mood)
        mood.save()
        messages.success(request, f'Mood {mood} Saved Successfully')
        return render(request, 'index.html')
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            loginFunc(request, user)
            messages.success(request, f'User {email} Logged In Successfully')
            return render(request, 'index.html')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'login.html')

    return render(request, 'login.html')



def signup(request):
    if request.method == 'POST':
            username = request.POST['username']
            firstName = request.POST['firstName']
            lastName = request.POST['lastName']
            email = request.POST['email']
            password = request.POST['password']
            try:
                createdUser = User.objects.create_user(username=username, email=email, password=password, first_name=firstName, last_name=lastName)
                createdUser.save()
                messages.success(request, f'User for {firstName} Created Successfully')
                return render(request, 'login.html')
            except Exception as e:
                print(e)
                return render(request, 'signup.html')

    return render(request, 'signup.html')


def logoutUser(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return render(request, 'index.html')


def assignments(request):
    act_user = request.user
    assignments = Assignemnt.objects.filter(user=act_user)
    param = {'assignments': assignments}
    if request.method == 'POST':
        assignmentName = request.POST['assignment']
        assignmentFile = request.FILES.get('file')
        user = request.user
        assignment = Assignemnt.objects.create(user=user, assignmentName=assignmentName, assigmentFile=assignmentFile)
        assignment.save()
        messages.success(request, f'Assignment {assignmentName} Saved Successfully')
        return render(request, 'assignments.html', param)
    return render(request, 'assignments.html', param)

def notes(request):
    act_user = request.user
    notes = Notes.objects.filter(user=act_user)
    param = {'notes': notes}
    if request.method == 'POST':
        noteName = request.POST['note']
        noteFile = request.FILES.get('file')
        user = request.user
        note = Notes.objects.create(user=user, noteName=noteName, noteFile=noteFile)
        note.save()
        messages.success(request, f'Assignment {noteName} Saved Successfully')
        return render(request, 'notes.html', param)
    return render(request, 'notes.html', param)

def journals(request):
    form = jounralForm()
    act_user = request.user
    journal = Journal.objects.filter(user=act_user)
    param = {'journals': journal, 'form': form}
    if request.method == 'POST':
        journalName = request.POST['journalName']
        journalFile = request.POST['journalFile']
        user = request.user
        journal = Journal.objects.create(user=user, journalName=journalName, journalFile=journalFile)
        journal.save()
        messages.success(request, f'Assignment {journalName} Saved Successfully')
        return render(request, 'journals.html', param)
    return render(request, 'journals.html', param)


def journalView(request, id):
    journal = Journal.objects.get(id=id)
    param = {'journal': journal}
    return render(request, 'journalView.html', param)
