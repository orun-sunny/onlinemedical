from math import ceil

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout as django_logout

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm, ProfileSearchForm,  Status_Form

# Create your views here.
# from django.views.generic.edit import TemplateView
from .models import Profile, Status


def search(request):

    query=request.GET['query']
    if len(query)> 50:
        messages.error(request, f'Accunt Created For {request.username}')

    else:
        users=User.objects.filter(username__icontains=query)


    context={'user':users,'query': query}
    return render(request,'counseling/ProfileFilterView.html' ,context)



def ProfileFilterView(request):

    users = User.objects.all()

    context = { 'user': users,
               }

    return render(request,'counseling/ProfileFilterView.html' ,context)


def index(request):
    form = ProfileEditForm()
    profiles = Profile.objects.all()
    users = User.objects.all()
    list = [users]

    n = len(users)
    nslides = n // 5 + ceil((n / 5) - (n // 5))
    params = {'no_of_slides': nslides, 'range': range(1, nslides), 'user': users, 'form': form, 'profile': profiles,
              'list': list}
    return render(request, 'counseling/index.html', params)


def about(request):
    return render(request, 'counseling/about.html')


def base(request):
    return render(request, 'counseling/base.html')


@login_required(login_url='/log')
def profile(request,i):
    u=User.objects.filter(username=i).first()
    context={'u':u}

    return render(request, 'counseling/profile.html',context)


@login_required(login_url='/log')
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserEditForm(data=request.POST or None, instance=request.user)
        p_form = ProfileEditForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('home')

    else:
        u_form = UserEditForm(instance=request.user)
        p_form = ProfileEditForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'counseling/profile_edit.html', context)


def signlog(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Accunt Created For {username}')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'counseling/signlog.html', {'form': form})

def post_write(request,i):
    if request.method == 'POST':
        s_form = Status_Form(request.POST,files=request.FILES)
        if s_form.is_valid():

            a=s_form.save(commit=False)
            a.user=request.user
            a.save()

            return redirect('blog')
    if request.method == 'GET':
        s_form=Status_Form()

    context = {
        's_form': s_form

    }
    return render(request, 'counseling/post-write.html', context)

def blog(request):

    status = Status.objects.all()


    context = {'status': status}

    return render(request, 'counseling/blog.html',context)
def department(request):
    return render(request, 'counseling/department.html')
def contact(request):
    return render(request, 'counseling/contact.html')


def blog_single(request,i):
    status=Status.objects.filter(id=i).first()
    context={'status':status}

    return render(request,'counseling/blog-single.html',context)


def gallery(request):
    return render(request, 'counseling/gallery.html')
def services(request):
    return render(request, 'counseling/services.html')


