from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_projects', '0002_rename_image_to_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='repository_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='demo_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='destaque',
            field=models.BooleanField(default=False),
        ),
    ]
