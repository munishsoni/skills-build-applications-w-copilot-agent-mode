from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='Running', duration=30, date=timezone.now())
        Activity.objects.create(user=users[1], activity_type='Cycling', duration=45, date=timezone.now())
        Activity.objects.create(user=users[2], activity_type='Swimming', duration=60, date=timezone.now())
        Activity.objects.create(user=users[3], activity_type='Yoga', duration=40, date=timezone.now())

        # Create Workouts
        w1 = Workout.objects.create(name='Super Strength', description='Strength workout for superheroes')
        w2 = Workout.objects.create(name='Agility Training', description='Agility workout for superheroes')
        w1.suggested_for.set([marvel, dc])
        w2.suggested_for.set([marvel, dc])

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
