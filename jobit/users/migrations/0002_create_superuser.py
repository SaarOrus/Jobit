from django.db import migrations, transaction
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile


def create_users_and_superuser(apps, schema_editor):
    with transaction.atomic():
        # Create a super user if it doesn't exist
        if not User.objects.filter(username='adminUser').exists():
            superuser = User.objects.create_superuser(
            username='adminUser', email='admin@gmail.com', password='adminPassword')
            superuser.profile.date_of_birth=timezone.now().date()
            superuser.profile.profession='SuperUser'
            superuser.profile.address='123 Super Lane'
            superuser.profile.gender='0'

        # Create normal users if they don't exist
        users_test_data = [
            ("yulisuliman", "Yuli", "Suliman", "yuli1234",
             "yuli@gmail.com", "profile_pics/yulisuliman.jpg", timezone.datetime(year=1999, month=8, day=6), "Software Developer", "New York", "F"),
            ("saarorus", "Saar", "Orus", "saar1234",
             "saar@gmail.com", "profile_pics/saarorus.jpg", timezone.datetime(year=1999, month=8, day=31), "Backend Developer", "New York", "F"),
            ("adirozenberg", "Adi", "Rozenberg", "adi1234",
             "adi@gmail.com", "profile_pics/adirozenberg.jpg", timezone.datetime(year=1998, month=7, day=3), "Software Developer", "New York", "F"),
            ("drormargalit", "Dror", "Margalit", "dror1234",
             "dror@gmail.com", "profile_pics/drormargalit.jpg", timezone.datetime(year=1998, month=12, day=3), "Doctor", "Tel Aviv", "M"),
            ("avihayun", "Avi", "Hayun", "avi1234",
             "avi@gmail.com", "default.jpg", timezone.datetime(year=1995, month=6, day=18), "Graphic Designer", "Haifa",
             "M")
        ]
        for username, first_name, last_name, password, email, profile_pic, dob, profession, address, gender in users_test_data:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name, last_name=last_name)
                user.profile.image=profile_pic
                user.profile.date_of_birth=dob
                user.profile.profession=profession
                user.profile.address=address
                user.profile.gender=gender
                user.profile.save()


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [migrations.RunPython(create_users_and_superuser)]
