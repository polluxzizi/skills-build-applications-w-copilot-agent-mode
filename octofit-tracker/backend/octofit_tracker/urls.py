import os

from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ActivityViewSet,
    LeaderboardViewSet,
    TeamViewSet,
    UserViewSet,
    WorkoutViewSet,
)

codespace_name = os.environ.get('CODESPACE_NAME')
codespace_base_url = (
    f"https://{codespace_name}-8000.app.github.dev" if codespace_name else "http://localhost:8000"
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutViewSet, basename='workout')


def api_root(request):
    return JsonResponse(
        {
            'base_url': codespace_base_url,
            'users': f'{codespace_base_url}/api/users/',
            'teams': f'{codespace_base_url}/api/teams/',
            'activities': f'{codespace_base_url}/api/activities/',
            'leaderboard': f'{codespace_base_url}/api/leaderboard/',
            'workouts': f'{codespace_base_url}/api/workouts/',
        }
    )

urlpatterns = [
    path('', api_root, name='root'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
