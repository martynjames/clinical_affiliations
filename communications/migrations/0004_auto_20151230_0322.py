# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import communications.models


class Migration(migrations.Migration):

    dependencies = [
        ('communications', '0003_communication_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(max_length=255, null=True, blank=True)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=100)),
                ('beds', models.IntegerField()),
                ('singles', models.IntegerField(null=True, blank=True)),
                ('shared', models.IntegerField(null=True, blank=True)),
                ('rotation_info', models.TextField(null=True, blank=True)),
                ('housing_contact', models.OneToOneField(null=True, blank=True, to='communications.Contact')),
                ('institution', models.ForeignKey(to='communications.Institution')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('paid_to', models.CharField(max_length=1024)),
                ('institution', models.ForeignKey(to='communications.Institution')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rotation_type', models.CharField(default=None, max_length=4, choices=[(b'MED', b'Medicine'), (b'SURG', b'Surgery'), (b'PEDS', b'Pediatrics'), (b'FAM', b'Family Medicine'), (b'OBGN', b'OB/GYN'), (b'PSYC', b'Psychiatry'), (b'NEUR', b'Neurology'), (b'RADI', b'Radiology'), (b'PA', b'PA'), (b'ELEC', b'Elective')])),
                ('number_of_students', models.IntegerField()),
                ('annual_number_of_rotations', models.IntegerField()),
                ('details', models.TextField(null=True, blank=True)),
                ('institution', models.ForeignKey(to='communications.Institution')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contact',
            name='administrative_contact',
            field=communications.models.InstitutionUniqueBooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='appointment_finalized',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='appointment_packet_submitted',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='buid_form_submitted',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='ceo',
            field=communications.models.InstitutionUniqueBooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='faculty_for_rotation',
            field=models.ForeignKey(blank=True, to='communications.Rotation', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='primary_contact',
            field=communications.models.InstitutionUniqueBooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='institution',
            name='agreement_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='institution',
            name='annual_admissions',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='institution',
            name='annual_emergency_visits',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='institution',
            name='annual_outpatient_visits',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='institution',
            name='average_stay',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='institution',
            name='bed_count',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='institution',
            name='major_affiliate',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='institution',
            name='occupancy_rate',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='communication',
            name='details',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='active_since',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='appointment_status',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='details',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='institution',
            field=models.ForeignKey(blank=True, to='communications.Institution', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='number_of_students',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='institution',
            name='address_2',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
