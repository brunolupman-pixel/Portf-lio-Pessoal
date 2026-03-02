from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='image',
            new_name='imagem',
        ),
    ]
