
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import AgentProfileForm, AgentSignupForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from properties.models import Property
from properties.forms import PropertyForm 
from .models import Profile


def signup(request):
    if request.method == 'POST':
        form = AgentSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Save phone to Profile
            phone = form.cleaned_data.get('phone')
            Profile.objects.create(user=user, phone=phone)
            login(request, user)
            return redirect('agent_dashboard')
    else:
        form = AgentSignupForm()
    return render(request, 'agents/signup.html', {'form': form})


@login_required
def agent_dashboard(request):
    my_properties = Property.objects.filter(agent=request.user)
    return render(request, 'agents/agent_dashboard.html', {'properties': my_properties})


@login_required
def edit_profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = AgentProfileForm(request.POST, user=request.user, profile=profile)
        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.save(update_fields=['email'])

            profile, _ = Profile.objects.get_or_create(user=request.user)
            profile.phone = form.cleaned_data['phone']
            profile.save(update_fields=['phone'])

            new_password = form.cleaned_data['new_password']
            if new_password:
                request.user.set_password(new_password)
                request.user.save(update_fields=['password'])
                login(request, request.user)
            return redirect('agent_dashboard')
    else:
        form = AgentProfileForm(user=request.user, profile=profile)
    return render(request, 'agents/edit_profile.html', {'form': form})

@login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.agent = request.user
            try:
                property.contact = request.user.profile.phone
            except:
                property.contact = request.user.email # fallback
            property.save()
            return redirect('agent_dashboard')
    else:
        form = PropertyForm()
    return render(request, 'agents/add_property.html', {'form': form})