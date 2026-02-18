from datetime import date

from django.test import TestCase
from rest_framework.test import APIClient

from .models import Activity, Leaderboard, Team, User, Workout


class OctofitModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Team Marvel', description='Marvel super heroes')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@test.com', team=self.team)

    def test_create_related_collections(self):
        workout = Workout.objects.create(
            user=self.user,
            title='Web Swing HIIT',
            difficulty='Intermediate',
            duration_minutes=35,
        )
        activity = Activity.objects.create(
            user=self.user,
            team=self.team,
            activity_type='Cardio',
            duration_minutes=35,
            calories_burned=420,
            activity_date=date(2026, 2, 16),
        )
        row = Leaderboard.objects.create(user=self.user, team=self.team, score=420, rank=1)

        self.assertEqual(Workout.objects.count(), 1)
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(Leaderboard.objects.count(), 1)
        self.assertEqual(workout.user_id, self.user.id)
        self.assertEqual(activity.team_id, self.team.id)
        self.assertEqual(row.rank, 1)


class OctofitApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Team DC', description='DC super heroes')
        self.user = User.objects.create(name='Batman', email='batman@test.com', team=self.team)

    def test_api_root_available(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.json())

    def test_users_endpoint_available(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
