# Generated by Django 4.0.3 on 2022-04-06 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token_book',
            name='token_number',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Admin_Token_Book',
        ),
    ]
