# Generated by Django 2.2.24 on 2022-04-29 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0142_auto_20220420_0336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchpledge',
            name='active',
        ),
        migrations.RemoveField(
            model_name='matchpledge',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='matchpledge',
            name='clr_round_num',
        ),
        migrations.RemoveField(
            model_name='matchpledge',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='matchpledge',
            name='data',
        ),
        migrations.RemoveField(
            model_name='matchpledge',
            name='pledge_type',
        ),
        migrations.RemoveField(
            model_name='matchpledge',
            name='profile',
        ),
    ]