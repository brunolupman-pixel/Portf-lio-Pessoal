from django.core.management.base import BaseCommand
from apps.profile.models import Profile
from apps.projects.models import Technology, Project
from apps.academic.models import AcademicBackground
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the database with sample bio, technologies, projects, and academic records.'

    def handle(self, *args, **options):
        # 1 bio
        if not Profile.objects.exists():
            bio = Profile.objects.create(
                name='Bruno Luppi Mancinelli',
                foto='',  # Set to empty, or upload manually
                role='Desenvolvedor Full-Stack',
                description='Desenvolvedor apaixonado por tecnologia, com experiência em projetos acadêmicos e profissionais.',
                email='brunolupman@email.com',
                linkedin='https://linkedin.com/in/bruno',
                github='https://github.com/brunolupman',
            )
            self.stdout.write(self.style.SUCCESS('Bio criado.'))
        else:
            bio = Profile.objects.first()
            self.stdout.write(self.style.WARNING('Bio já existe.'))

        # 3 technologies
        tech_names = ['Django', 'React', 'PostgreSQL']
        tech_objs = []
        for name in tech_names:
            tech, _ = Technology.objects.get_or_create(name=name)
            tech_objs.append(tech)
        self.stdout.write(self.style.SUCCESS('Tecnologias criadas.'))

        # 3 projects
        project_data = [
            {
                'title': 'Portfolio Pessoal',
                'description': 'Site para apresentar projetos, formação e contato.',
                'destaque': True,
                'repository_url': 'https://github.com/brunolupman-pixel/Portf-lio-Pessoal',
                'demo_url': '',
                'imagem': '',
                'technologies': tech_objs[:2],
            },
            {
                'title': 'Sistema Acadêmico',
                'description': 'Gerenciador de registros acadêmicos.',
                'destaque': False,
                'repository_url': '',
                'demo_url': '',
                'imagem': '',
                'technologies': tech_objs[1:],
            },
            {
                'title': 'API de Contato',
                'description': 'Backend para mensagens de contato.',
                'destaque': False,
                'repository_url': '',
                'demo_url': '',
                'imagem': '',
                'technologies': tech_objs[:1],
            },
        ]
        for pdata in project_data:
            proj, created = Project.objects.get_or_create(
                title=pdata['title'],
                defaults={
                    'description': pdata['description'],
                    'destaque': pdata['destaque'],
                    'repository_url': pdata['repository_url'],
                    'demo_url': pdata['demo_url'],
                    'imagem': pdata['imagem'],
                }
            )
            proj.technologies.set(pdata['technologies'])
        self.stdout.write(self.style.SUCCESS('Projetos criados.'))

        # 2 academic records
        academic_data = [
            {
                'profile': bio,
                'institution': 'Universidade Federal',
                'course': 'Engenharia de Software',
                'description': 'Graduação em Engenharia de Software.',
                'start_date': timezone.datetime(2022, 2, 1),
                'end_date': timezone.datetime(2026, 12, 1),
            },
            {
                'profile': bio,
                'institution': 'Instituto Técnico',
                'course': 'Técnico em Informática',
                'description': 'Curso técnico profissionalizante.',
                'start_date': timezone.datetime(2020, 2, 1),
                'end_date': timezone.datetime(2021, 12, 1),
            },
        ]
        for adata in academic_data:
            AcademicBackground.objects.get_or_create(
                profile=adata['profile'],
                institution=adata['institution'],
                course=adata['course'],
                defaults={
                    'description': adata['description'],
                    'start_date': adata['start_date'],
                    'end_date': adata['end_date'],
                }
            )
        self.stdout.write(self.style.SUCCESS('Formação acadêmica criada.'))
