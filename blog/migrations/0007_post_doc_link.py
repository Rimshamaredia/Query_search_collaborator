# Generated by Django 4.0 on 2022-12-06 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_tags_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='doc_link',
            field=models.URLField(default='https://docs.google.com/document/d/1PYSkN38yVxokq8gk4exA5fiT-cmCdASpP5_weZ9ThLs/edit'),
        ),
    ]
