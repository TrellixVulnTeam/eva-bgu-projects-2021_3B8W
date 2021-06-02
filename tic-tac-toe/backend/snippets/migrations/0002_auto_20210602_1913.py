# Generated by Django 3.2.4 on 2021-06-02 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snippet',
            options={'ordering': ('created',)},
        ),
        migrations.RenameField(
            model_name='snippet',
            old_name='code',
            new_name='winner',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='highlighted',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='language',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='linenos',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='style',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='title',
        ),
    ]
