from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='photo',
            new_name='foto',
        ),
    ]
