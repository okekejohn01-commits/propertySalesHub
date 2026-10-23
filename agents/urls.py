from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.agent_dashboard, name='agent_dashboard'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('add/', views.add_property, name='add_property'),
]

