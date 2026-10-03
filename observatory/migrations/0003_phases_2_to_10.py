from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('observatory', '0002_add_location_source_updated_at'),
    ]

    operations = [
        # Phase 9 — Organisation (created first; Signal will FK to it)
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('website', models.URLField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['name'], 'verbose_name': 'Organisation', 'verbose_name_plural': 'Organisations'},
        ),
        # Phase 3 — Geospatial fields on IntelligenceSignal
        migrations.AddField(
            model_name='intelligencesignal',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='intelligencesignal',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        # Phase 9 — Organisation FK on IntelligenceSignal
        migrations.AddField(
            model_name='intelligencesignal',
            name='organisation',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='signals',
                to='observatory.organisation',
            ),
        ),
        # Phase 2 — Evidence
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('evidence_type', models.CharField(
                    choices=[('Observation', 'Observation'), ('Report', 'Report'), ('Data', 'Data'),
                             ('Testimony', 'Testimony'), ('Media', 'Media'), ('Other', 'Other')],
                    default='Observation', max_length=50,
                )),
                ('reliability', models.CharField(
                    choices=[('Unverified', 'Unverified'), ('Plausible', 'Plausible'), ('Confirmed', 'Confirmed')],
                    default='Unverified', max_length=50,
                )),
                ('description', models.TextField(blank=True)),
                ('source_url', models.URLField(blank=True)),
                ('collected_at', models.DateTimeField(auto_now_add=True)),
                ('signal', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='evidence',
                    to='observatory.intelligencesignal',
                )),
            ],
            options={'ordering': ['-collected_at'], 'verbose_name': 'Evidence', 'verbose_name_plural': 'Evidence'},
        ),
        # Phase 5 — Assessment
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField()),
                ('priority', models.CharField(
                    choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')],
                    default='Medium', max_length=20,
                )),
                ('recommendation', models.TextField(blank=True)),
                ('assessed_by', models.CharField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('signal', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='assessment',
                    to='observatory.intelligencesignal',
                )),
            ],
            options={'ordering': ['-created_at'], 'verbose_name': 'Assessment', 'verbose_name_plural': 'Assessments'},
        ),
        # Phase 4 — Opportunity
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(
                    choices=[('Identified', 'Identified'), ('Scoping', 'Scoping'), ('Ready', 'Ready'),
                             ('Active', 'Active'), ('Closed', 'Closed')],
                    default='Identified', max_length=50,
                )),
                ('location', models.CharField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('signal', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='opportunities',
                    to='observatory.intelligencesignal',
                )),
            ],
            options={'ordering': ['-created_at'], 'verbose_name': 'Opportunity', 'verbose_name_plural': 'Opportunities'},
        ),
        # Phase 7 — ActionItem
        migrations.CreateModel(
            name='ActionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('assigned_to', models.CharField(blank=True, max_length=200)),
                ('status', models.CharField(
                    choices=[('Proposed', 'Proposed'), ('Assigned', 'Assigned'), ('In Progress', 'In Progress'),
                             ('Complete', 'Complete'), ('Cancelled', 'Cancelled')],
                    default='Proposed', max_length=50,
                )),
                ('due_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('opportunity', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='actions',
                    to='observatory.opportunity',
                )),
            ],
            options={'ordering': ['due_date', '-created_at'], 'verbose_name': 'Action Item', 'verbose_name_plural': 'Action Items'},
        ),
        # Phase 8 — ImpactRecord
        migrations.CreateModel(
            name='ImpactRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('impact_type', models.CharField(
                    choices=[('Environmental', 'Environmental'), ('Social', 'Social'),
                             ('Economic', 'Economic'), ('Institutional', 'Institutional')],
                    max_length=50,
                )),
                ('description', models.TextField(blank=True)),
                ('metric', models.CharField(blank=True, max_length=200)),
                ('recorded_at', models.DateTimeField(auto_now_add=True)),
                ('action', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='impacts',
                    to='observatory.actionitem',
                )),
            ],
            options={'ordering': ['-recorded_at'], 'verbose_name': 'Impact Record', 'verbose_name_plural': 'Impact Records'},
        ),
    ]
