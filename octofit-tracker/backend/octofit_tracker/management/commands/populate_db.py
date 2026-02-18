from datetime import date

from django.core.management.base import BaseCommand

from octofit_tracker.models import Activity, Leaderboard, Team, User, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        marvel = Team.objects.create(name='Team Marvel', description='Marvel super heroes')
        dc = Team.objects.create(name='Team DC', description='DC super heroes')

        heroes = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': marvel},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': marvel},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': dc},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': dc},
        ]

        users = [User.objects.create(**hero) for hero in heroes]

        Workout.objects.bulk_create(
            [
                Workout(user=users[0], title='Web Swing HIIT', difficulty='Intermediate', duration_minutes=35),
                Workout(user=users[1], title='Arc Reactor Strength', difficulty='Advanced', duration_minutes=45),
                Workout(user=users[2], title='Amazon Endurance', difficulty='Advanced', duration_minutes=40),
                Workout(user=users[3], title='Gotham Night Run', difficulty='Intermediate', duration_minutes=30),
            ]
        )

        Activity.objects.bulk_create(
            [
                Activity(
                    user=users[0],
                    team=marvel,
                    activity_type='Cardio',
                    duration_minutes=35,
                    calories_burned=420,
                    activity_date=date(2026, 2, 16),
                ),
                Activity(
                    user=users[1],
                    team=marvel,
                    activity_type='Strength',
                    duration_minutes=45,
                    calories_burned=560,
                    activity_date=date(2026, 2, 16),
                ),
                Activity(
                    user=users[2],
                    team=dc,
                    activity_type='Mixed',
                    duration_minutes=40,
                    calories_burned=510,
                    activity_date=date(2026, 2, 17),
                ),
                Activity(
                    user=users[3],
                    team=dc,
                    activity_type='Cardio',
                    duration_minutes=30,
                    calories_burned=350,
                    activity_date=date(2026, 2, 17),
                ),
            ]
        )

        Leaderboard.objects.bulk_create(
            [
                Leaderboard(user=users[1], team=marvel, score=560, rank=1),
                Leaderboard(user=users[2], team=dc, score=510, rank=2),
                Leaderboard(user=users[0], team=marvel, score=420, rank=3),
                Leaderboard(user=users[3], team=dc, score=350, rank=4),
            ]
        )

        self.stdout.write(self.style.SUCCESS('octofit_db populated with sample superhero data'))
