<<<<<<< HEAD
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from apps.profile.views import ProfileViewSet
from apps.projects.views import ProjectViewSet, TechnologyViewSet
from apps.academic.views import AcademicBackgroundViewSet
from apps.contact.views import ContactMessageCreateView

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'academic', AcademicBackgroundViewSet, basename='academic')
router.register(r'technologies', TechnologyViewSet, basename='technologies')

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', ContactMessageCreateView.as_view(), name='contact-create'),
]
=======
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from apps.profile.views import ProfileViewSet
from apps.projects.views import ProjectViewSet, TechnologyViewSet
from apps.academic.views import AcademicBackgroundViewSet
from apps.contact.views import ContactMessageCreateView

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'academic', AcademicBackgroundViewSet, basename='academic')
router.register(r'technologies', TechnologyViewSet, basename='technologies')

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', ContactMessageCreateView.as_view(), name='contact-create'),
]
>>>>>>> origin/main
