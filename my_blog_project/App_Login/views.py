from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Login.forms import SignUpForm, ProfileUpdateForm,ProfilePic

# Create your views here.

def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    diction = {'form':form,'registered':registered}
    return render(request,'App_Login/sign_up.html',context = diction)


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    diction = {'form':form}
    return render(request,'App_Login/login.html',context=diction)


@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    diction = {}
    return render(request,'App_Login/profile.html',context = diction)


@login_required
def update_profile(request):
    current_user = request.user
    form = ProfileUpdateForm(instance = current_user)

    if request.method == 'POST':
        form = ProfileUpdateForm(data = request.POST, instance = current_user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    diction = {'form':form}
    return render(request,'App_Login/update_profile.html',context=diction)


@login_required
def password_change(request):
    changed = False
    current_user = request.user
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user,data=request.POST)

        if form.is_valid():
            form.save()
            changed = True


    return render(request,'App_Login/password_change.html',context={'form':form,'changed':changed})



@login_required
def add_pro_pic(request):
    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit = False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'App_Login/add_pro_pic.html',context={'form':form})


@login_required
def change_pro_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES, instance = request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))

    return render(request,'App_Login/add_pro_pic.html',context={'form':form})
