from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# ----- frontend pages -----
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.urls import reverse_lazy
from apps.projects.models import Project
from apps.academic.models import AcademicBackground
from apps.contact.forms import ContactMessageForm


def home(request):
    profile = Profile.objects.first()
    highlights = Project.objects.filter(destaque=True).order_by('-created_at').prefetch_related('technologies')
    return render(request, 'home.html', {'profile': profile, 'highlights': highlights})


class ProjectsListView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'
    queryset = Project.objects.all().prefetch_related('technologies').order_by('-created_at')


class AcademicListView(ListView):
    model = AcademicBackground
    template_name = 'academic.html'
    context_object_name = 'formations'
    queryset = AcademicBackground.objects.select_related('profile').order_by('-start_date')


def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('contact') + '?submitted=1')
    else:
        form = ContactMessageForm()
        if request.GET.get('submitted'):
            submitted = True
    return render(request, 'contact.html', {'form': form, 'submitted': submitted})