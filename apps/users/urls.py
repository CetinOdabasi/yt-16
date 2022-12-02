from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import registration_view, logout, detail_user, update_user

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('logout/', logout),
    path('detail/', detail_user),
    path('register/', registration_view, name="register"),
    path('update/', update_user),
]
