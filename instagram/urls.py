from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import current_user


urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        'current/',
        current_user,
        name='current_user'
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout',
    ),
    # DRF
    path(
        '',
        include('instagram.router_patterns')
    ),
    path(
        'auth',
        include('rest_framework.urls')
    ),
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair_view'
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh_view'
    )
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
