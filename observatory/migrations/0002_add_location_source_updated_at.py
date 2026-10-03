from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observatory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='intelligencesignal',
            name='location',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='intelligencesignal',
            name='source',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='intelligencesignal',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='intelligencesignal',
            name='category',
            field=models.CharField(
                choices=[
                    ('Water', 'Water'), ('Infrastructure', 'Infrastructure'),
                    ('Ecology', 'Ecology'), ('Food', 'Food'), ('Energy', 'Energy'),
                    ('Climate', 'Climate'), ('Community', 'Community'), ('Health', 'Health'),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name='intelligencesignal',
            name='status',
            field=models.CharField(
                choices=[
                    ('Observed', 'Observed'), ('Reviewing', 'Reviewing'),
                    ('Verified', 'Verified'), ('Actionable', 'Actionable'),
                    ('Resolved', 'Resolved'),
                ],
                default='Observed',
                max_length=50,
            ),
        ),
    ]
