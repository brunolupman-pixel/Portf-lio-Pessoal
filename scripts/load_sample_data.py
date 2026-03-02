"""Bootstrap sample data for the portfolio development environment.

Run with:

    python manage.py shell < scripts/load_sample_data.py

This will create one Profile, three Project instances and two AcademicBackground entries.
"""

from apps.profile.models import Profile
from apps.projects.models import Project, Technology
from apps.academic.models import AcademicBackground
from django.utils import timezone

# delete existing to avoid duplicates
Profile.objects.all().delete()
Project.objects.all().delete()
AcademicBackground.objects.all().delete()
Technology.objects.all().delete()

# create profile
profile = Profile.objects.create(
    name='João Silva',
    role='Desenvolvedor Full-Stack',
    description='Sou um desenvolvedor apaixonado por criar aplicações web modernas.',
    email='joao@example.com',
)

# technologies
techs = []
for name in ['Django', 'React', 'PostgreSQL', 'Docker']:
    techs.append(Technology.objects.create(name=name))

# projects
proj1 = Project.objects.create(
    title='Website Pessoal',
    description='Meu website pessoal construído com Django e React.',
    destaque=True,
)
proj1.tecnologias.set([techs[0], techs[1]])

proj2 = Project.objects.create(
    title='API REST',
    description='Uma API RESTful para gerenciamento de tarefas.',
    destaque=True,
)
proj2.tecnologias.set([techs[0], techs[2]])

proj3 = Project.objects.create(
    title='App de Chat',
    description='Aplicativo de chat em tempo real utilizando WebSockets.',
    destaque=False,
)
proj3.tecnologias.set([techs[0], techs[1], techs[3]])

# academic backgrounds
AcademicBackground.objects.create(
    profile=profile,
    course='Bacharel em Ciência da Computação',
    institution='Universidade Fictícia',
    start_date=timezone.datetime(2017, 1, 1),
    end_date=timezone.datetime(2020, 12, 31),
    description='Concentração em sistemas de informação.',
)
AcademicBackground.objects.create(
    profile=profile,
    course='Mestrado em Engenharia de Software',
    institution='Instituto de Tecnologia Avançada',
    start_date=timezone.datetime(2021, 2, 1),
    end_date=None,
    description='Pesquisas em metodologias ágeis.',
)

print('Sample data created!')