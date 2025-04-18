# Generated by Django 5.1.2 on 2024-10-26 21:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0094_alter_company_company_in_charge'),
        ('login', '0018_new_user_is_deleted_alter_consultant_token_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate1Status_not_eligible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='John', max_length=255)),
                ('last_name', models.CharField(default='Doe', max_length=255)),
                ('status', models.CharField(default='not_eligible', max_length=20)),
                ('college_id', models.IntegerField()),
                ('job_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Candidate1Status_rejected',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='John', max_length=255)),
                ('last_name', models.CharField(default='Doe', max_length=255)),
                ('status', models.CharField(default='rejected', max_length=20)),
                ('college_id', models.IntegerField()),
                ('job_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Candidate1Status_selected',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='John', max_length=255)),
                ('last_name', models.CharField(default='Doe', max_length=255)),
                ('status', models.CharField(default='selected', max_length=20)),
                ('college_id', models.IntegerField()),
                ('job_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Candidate1Status_under_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='John', max_length=255)),
                ('last_name', models.CharField(default='Doe', max_length=255)),
                ('status', models.CharField(default='under_review', max_length=20)),
                ('college_id', models.IntegerField()),
                ('job_id', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='usersubscription',
            name='current_plan',
        ),
        migrations.RemoveField(
            model_name='screeninganswer',
            name='application',
        ),
        migrations.RemoveField(
            model_name='screeninganswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='screeningquestion',
            name='job',
        ),
        migrations.RemoveField(
            model_name='usersubscription',
            name='user',
        ),
        migrations.RemoveField(
            model_name='application',
            name='student',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='student',
        ),
        migrations.RemoveField(
            model_name='job',
            name='card_number',
        ),
        migrations.RemoveField(
            model_name='job',
            name='country',
        ),
        migrations.RemoveField(
            model_name='job',
            name='expiration_code',
        ),
        migrations.RemoveField(
            model_name='job',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='job',
            name='gst',
        ),
        migrations.RemoveField(
            model_name='job',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='job',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='job',
            name='promoting_job',
        ),
        migrations.RemoveField(
            model_name='job',
            name='security_code',
        ),
        migrations.RemoveField(
            model_name='job1',
            name='card_number',
        ),
        migrations.RemoveField(
            model_name='job1',
            name='country',
        ),
        migrations.RemoveField(
            model_name='job1',
            name='expiration_code',
        ),
        migrations.RemoveField(
            model_name='job1',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='job1',
            name='gst',
        ),
        migrations.RemoveField(
            model_name='job1',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='job1',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='job1',
            name='promoting_job',
        ),
        migrations.RemoveField(
            model_name='job1',
            name='security_code',
        ),
        migrations.RemoveField(
            model_name='message',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.AddField(
            model_name='achievements',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.new_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='company_in_charge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.companyincharge'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='job_seeker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.jobseeker'),
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.new_user'),
        ),
        migrations.AddField(
            model_name='application1',
            name='job_seeker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.jobseeker'),
        ),
        migrations.AddField(
            model_name='application1',
            name='university_in_charge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.universityincharge'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application1',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.new_user'),
        ),
        migrations.AddField(
            model_name='certification',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.new_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='college',
            name='university_in_charge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.universityincharge'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collegeenquiry',
            name='university_in_charge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.universityincharge'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.new_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.new_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interview',
            name='company_in_charge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.companyincharge'),
        ),
        migrations.AddField(
            model_name='interview',
            name='job_seeker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.jobseeker'),
        ),
        migrations.AddField(
            model_name='interview',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.new_user'),
        ),
        migrations.AddField(
            model_name='job',
            name='company_in_charge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.companyincharge'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job1',
            name='university_in_charge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.universityincharge'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='company_recipient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recipient', to='job_portal.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='sender_job_seeker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.jobseeker'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender_new_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.new_user'),
        ),
        migrations.AddField(
            model_name='objective',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.new_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.new_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publications',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.new_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reference',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.new_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.new_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.new_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentenquiry',
            name='new_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.new_user'),
        ),
        migrations.AddField(
            model_name='studentenquiry',
            name='university_in_charge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.universityincharge'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitor',
            name='university_in_charge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.universityincharge'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='company_in_charge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.companyincharge'),
        ),
        migrations.AlterField(
            model_name='education',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education_entries', to='job_portal.resume'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience_entries', to='job_portal.resume'),
        ),
        migrations.CreateModel(
            name='College_Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('college_recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clg_recipient', to='job_portal.college')),
                ('sender_jobseeker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.jobseeker')),
                ('sender_newuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.new_user')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='College_Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='attachments/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachment', to='job_portal.college_message')),
            ],
        ),
        migrations.CreateModel(
            name='CollegeScreeningQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('correct_answer', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screening_questions', to='job_portal.job1')),
                ('university_in_charge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.universityincharge')),
            ],
        ),
        migrations.CreateModel(
            name='CollegeScreeningAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screening_answers', to='job_portal.application1')),
                ('university_in_charge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.universityincharge')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='job_portal.collegescreeningquestion')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyScreeningQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('correct_answer', models.TextField()),
                ('company_in_charge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.companyincharge')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screening_questions', to='job_portal.job')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyScreeningAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screening_answers', to='job_portal.application')),
                ('company_in_charge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.companyincharge')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='job_portal.companyscreeningquestion')),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker_Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='John', max_length=100)),
                ('last_name', models.CharField(default='John Doe', max_length=100)),
                ('email', models.EmailField(default='example@example.com', max_length=254)),
                ('phone', models.CharField(default='000-000-0000', max_length=20)),
                ('address', models.TextField(default='N/A')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('website_urls', models.JSONField(default=list)),
                ('skills', models.TextField(default='Not specified')),
                ('activities', models.TextField(default='None')),
                ('interests', models.TextField(default='None')),
                ('languages', models.TextField(default='None')),
                ('bio', models.TextField(default='None')),
                ('city', models.CharField(default='Mumbai', max_length=100)),
                ('state', models.CharField(default='Maharashtra', max_length=100)),
                ('country', models.CharField(default='India', max_length=100)),
                ('zipcode', models.CharField(default='522426', max_length=6)),
                ('Attachment', models.FileField(default='Unknown', upload_to='attachments/')),
                ('delete', models.BooleanField(default=False)),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.jobseeker')),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker_Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=100)),
                ('contact_info', models.CharField(default='Not provided', max_length=100)),
                ('relationship', models.CharField(default='N/A', max_length=100)),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.jobseeker')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='references', to='job_portal.jobseeker_resume')),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker_Publications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Unknown', max_length=100)),
                ('publisher', models.CharField(default='Unknown', max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.jobseeker')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='job_portal.jobseeker_resume')),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker_Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitled Project', max_length=100)),
                ('description', models.TextField(default='No description')),
                ('project_link', models.TextField(default=list)),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.jobseeker')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='job_portal.jobseeker_resume')),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker_Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='Not specified')),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.jobseeker')),
                ('resume', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='objective', to='job_portal.jobseeker_resume')),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker_Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(default='Unknown', max_length=100)),
                ('company_name', models.CharField(default='Unknown', max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(default='No description')),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.jobseeker')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience_entries', to='job_portal.jobseeker_resume')),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker_Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_or_degree', models.CharField(default='Unknown', max_length=100)),
                ('school_or_university', models.CharField(default='Unknown', max_length=100)),
                ('grade_or_cgpa', models.CharField(default='N/A', max_length=50)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(default='No description')),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.jobseeker')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education_entries', to='job_portal.jobseeker_resume')),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker_Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.jobseeker')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certifications', to='job_portal.jobseeker_resume')),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker_Achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Unknown', max_length=100)),
                ('publisher', models.CharField(default='Unknown', max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.jobseeker')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to='job_portal.jobseeker_resume')),
            ],
        ),
        migrations.DeleteModel(
            name='MembershipPlan',
        ),
        migrations.DeleteModel(
            name='ScreeningAnswer',
        ),
        migrations.DeleteModel(
            name='ScreeningQuestion',
        ),
        migrations.DeleteModel(
            name='UserSubscription',
        ),
    ]
