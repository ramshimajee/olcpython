# Generated by Django 5.1.1 on 2024-10-23 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0002_affiliates_annualreport_boardmembers_bylawtable_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membershipsubscription',
            old_name='membershiptypeid',
            new_name='membershiptype',
        ),
    ]