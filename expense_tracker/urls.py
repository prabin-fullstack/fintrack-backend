from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/accounts/', include('accounts.urls')),
    path('api/transactions/', include('transactions.urls')),

    path('api/accounts/login/', TokenObtainPairView.as_view()),
    path('api/accounts/token/refresh/', TokenRefreshView.as_view()),
]