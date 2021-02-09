# Generated by Django 2.2.17 on 2021-02-04 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0227_auto_20210126_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='consortium',
            field=models.BooleanField(default=False, help_text='Determines whether this is a group of organisations working together under a consortium.'),
        ),
        migrations.AddField(
            model_name='membership',
            name='emergency_contact',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='public_status',
            field=models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=20,
                                   verbose_name="Can this membership be publicized on The carpentries websites?",
                                   help_text="Public memberships may be listed on any of The Carpentries websites."
            ),
        ),
    ]
