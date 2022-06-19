from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from hood.forms import *
from django.contrib.auth.models import User
from hood.models import *
from django import forms
from django.http.response import Http404, HttpResponseRedirect
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.core.exceptions import ObjectDoesNotExist


# views here.
def index(request):
    current_user = request.user

    profiles = Profile.objects.filter(user_id = current_user.id).all()
    return render(request, 'index.html',{'profiles':profiles,})
    

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            prof.save()
            return redirect ('index')
        else:
            form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form}
    )
@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    ctx = {"profile": profile}
    return render(request, "profile.html", ctx)

@login_required(login_url="/accounts/login/")
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile')
    ctx = {"form":form}
    return render(request, 'update_profile.html', ctx)


