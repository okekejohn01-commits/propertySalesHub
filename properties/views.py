
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Property
from agents.models import Profile

def home(request):
    states = [
        'Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 
        'Benue', 'Borno', 'Cross River', 'Delta', 'Ebonyi', 'Edo', 
        'Ekiti', 'Enugu', 'FCT', 'Gombe', 'Imo', 'Jigawa', 'Kaduna', 
        'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 
        'Niger', 'Ogun', 'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 
        'Sokoto', 'Taraba', 'Yobe', 'Zamfara'
    ] # All 37 states

    properties = Property.objects.all()

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            properties = properties.filter(state=state)

    if 'property_type' in request.GET:
        p_type = request.GET['property_type']
        if p_type:
            properties = properties.filter(property_type=p_type)

    return render(request, 'properties/home.html', {'states': states, 'properties': properties})



def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    agent_phone = Profile.objects.filter(user_id=property.agent_id).values_list('phone', flat=True).first()
    return render(request, 'properties/detail.html', {
        'property': property,
        'agent_phone': agent_phone,
    })

def about(request):
    return render(request, 'properties/about.html')

