from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User(email='captain@marvel.com', name='Captain America', team='Marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='Marvel'),
            User(email='batman@dc.com', name='Batman', team='DC'),
            User(email='superman@dc.com', name='Superman', team='DC'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
        ]
        User.objects.bulk_create(users)

        # Activities
        activities = [
            Activity(user='Iron Man', activity_type='Running', duration=30),
            Activity(user='Captain America', activity_type='Cycling', duration=45),
            Activity(user='Spider-Man', activity_type='Jumping', duration=20),
            Activity(user='Batman', activity_type='Martial Arts', duration=60),
            Activity(user='Superman', activity_type='Flying', duration=120),
            Activity(user='Wonder Woman', activity_type='Strength', duration=50),
        ]
        Activity.objects.bulk_create(activities)

        # Workouts
        workouts = [
            Workout(name='Hero HIIT', difficulty='Hard'),
            Workout(name='Power Yoga', difficulty='Medium'),
            Workout(name='Speed Run', difficulty='Easy'),
        ]
        Workout.objects.bulk_create(workouts)

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=95)
        Leaderboard.objects.create(team='DC', points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
