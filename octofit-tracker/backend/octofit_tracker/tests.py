from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team', description='desc')
        self.assertEqual(str(team), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(name='U', email='u@test.com', team=team, is_superhero=True)
        self.assertEqual(str(user), 'U')
    def test_activity_create(self):
        team = Team.objects.create(name='T2', description='d2')
        user = User.objects.create(name='U2', email='u2@test.com', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, activity_type='Run', duration=10, date='2026-01-11')
        self.assertIn('Run', str(activity))
    def test_workout_create(self):
        team = Team.objects.create(name='T3', description='d3')
        workout = Workout.objects.create(name='W', description='desc')
        workout.suggested_for.set([team])
        self.assertEqual(str(workout), 'W')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='T4', description='d4')
        leaderboard = Leaderboard.objects.create(team=team, points=42)
        self.assertIn('T4', str(leaderboard))
