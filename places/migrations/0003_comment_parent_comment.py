# Generated by Django 4.2.4 on 2023-09-12 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_category_options_alter_gallery_options_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='master_comment', to='places.comment'),
        ),
    ]
