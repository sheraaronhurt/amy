# Generated by Django 2.2.18 on 2021-05-09 20:51

from django.db import migrations, models


def find_duplicate_members(apps, schema_editor):
    """The next migration will enforce a unique constraint in DB, which may result in
    database server rejecting migration in case there are some duplicate entries. This
    function will try to find them and report."""
    Member = apps.get_model("workshops", "Member")
    duplicates = (
        Member.objects.values("membership", "organization", "role")
        .annotate(count=models.Count("id"))
        .values("membership", "organization", "role")
        .order_by()
        .filter(count__gt=1)
    )
    if duplicates:
        print("\n>>> FOUND DUPLICATES IN MEMBERS! <<<")
        for value in duplicates:
            print(value)


class Migration(migrations.Migration):

    dependencies = [
        ("workshops", "0243_auto_20210508_1954"),
    ]

    operations = [
        migrations.RunPython(find_duplicate_members, migrations.RunPython.noop),
        migrations.AddConstraint(
            model_name="member",
            constraint=models.UniqueConstraint(
                fields=("membership", "organization", "role"),
                name="unique_member_role_in_membership",
            ),
        ),
    ]
