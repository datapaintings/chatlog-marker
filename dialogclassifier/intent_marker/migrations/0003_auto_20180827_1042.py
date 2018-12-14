# Generated by Django 2.1 on 2018-08-27 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intent_marker', '0002_auto_20180827_1040'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='parseddialogs',
            index=models.Index(fields=['cus_id'], name='intent_mark_cus_id_8307c6_idx'),
        ),
        migrations.AddIndex(
            model_name='parseddialogs',
            index=models.Index(fields=['dialog_time'], name='intent_mark_dialog__2304cf_idx'),
        ),
        migrations.AddIndex(
            model_name='parseddialogs',
            index=models.Index(fields=['cus_id', 'dialog_time'], name='intent_mark_cus_id_540e08_idx'),
        ),
    ]