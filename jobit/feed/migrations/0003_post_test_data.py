from django.utils import timezone
from datetime import datetime

from django.db import migrations, transaction
from django.contrib.auth.models import User

from feed.models import Comment, Post


class Migration(migrations.Migration):
    dependencies = [
        ('feed', '0002_delete_category'), ('users', '0002_create_superuser'),
    ]

    def post_test_data(apps, schema_editor):
        with transaction.atomic():
            # Gas station worker job post
            adi_post = Post.objects.create(
                title='Gas Station Worker Needed',
                content='We are looking for a gas station worker who is helpful and nice.',
                category='Retail',
                location='Tel Aviv',
                date_posted=datetime.now(tz=timezone.utc),
                requirements='No prior experience required.',
                author=User.objects.get(username='adirozenberg')
            )

            # Dishwasher job post
            saar_post = Post.objects.create(
                title='Dishwasher Needed at FISH Restaurant',
                content='We are hiring a dishwasher for our Rishon Lezion location.',
                category='Food Services',
                location='Rishon Lezion',
                date_posted=datetime.now(tz=timezone.utc),
                requirements='No prior experience required.',
                author=User.objects.get(username='saarorus')
            )

            # House painter job post
            yuli_post = Post.objects.create(
                title='Worker Needed for House Painting',
                content='We are looking for a worker to help paint a house. Physical work, no experience required.',
                category='Home Services',
                location='Jerusalem',
                date_posted=datetime.now(tz=timezone.utc),
                requirements='No prior experience required.',
                author=User.objects.get(username='yulisuliman')
            )
            dror_post = Post.objects.create(
                title='Computer Science Project Reviewer Needed',
                content='We are looking for a student with a bachelor\'s degree in computer science to review projects. Please contact us if you are interested.',
                category='Other',
                date_posted=datetime.now(tz=timezone.utc),
                author=User.objects.get(username='drormargalit'),
                location='Home',
                salary='45 shekels per hour',
                requirements='Graduated with a bachelor\'s degree in computer science',
                header_image=None
            )

            yuli_post.save()
            adi_post.save()
            saar_post.save()
            dror_post.save()

            comment1 = Comment(post=yuli_post, name='Rachel',
                               body='This job sounds great! I have experience with graphic design and would love to apply. Can you please provide more information on how to apply?')
            comment2 = Comment(post=adi_post, name='Avi',
                               body='I am interested in this job! Can you please let me know what the salary range is and what the hours would be?')
            comment3 = Comment(post=saar_post, name='Maya',
                               body='The job sounds right to me! Is it possible to work only in evening shifts?')
            comment4 = Comment(post=dror_post, name='Shai',
                               body='I\'m intrigued by this job opportunity! Can you provide more information about the type of projects involved and what the timeline would be?')

            comment1.save()
            comment2.save()
            comment3.save()
            comment4.save()

    operations = [
        migrations.RunPython(post_test_data),
    ]
