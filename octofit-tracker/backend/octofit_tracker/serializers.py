from rest_framework import serializers

from .models import Activity, Leaderboard, Team, User, Workout


class ObjectIdStringSerializerMixin:
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj.pk)


class TeamSerializer(ObjectIdStringSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description']


class UserSerializer(ObjectIdStringSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team']


class WorkoutSerializer(ObjectIdStringSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'user', 'title', 'difficulty', 'duration_minutes']


class ActivitySerializer(ObjectIdStringSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'user', 'team', 'activity_type', 'duration_minutes', 'calories_burned', 'activity_date']


class LeaderboardSerializer(ObjectIdStringSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'team', 'score', 'rank']
