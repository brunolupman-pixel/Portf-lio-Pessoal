from django.urls import path
from apps.profile import views as profile_views

urlpatterns = [
    path('', profile_views.home, name='home'),
    path('projetos/', profile_views.ProjectsListView.as_view(), name='projects'),
    path('formacao/', profile_views.AcademicListView.as_view(), name='academic'),
    path('contato/', profile_views.contact, name='contact'),
]
