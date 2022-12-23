from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),

    path(('api/v1/auth/'), include('users.urls')),

    path('api/v1/password-reset/', PasswordResetView.as_view()),
    path('api/v1/password-reset-confirm/<slug:uidb64>/<slug:token>/',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]
