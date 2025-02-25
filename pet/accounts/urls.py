from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import employee_info, login_view, register_view

urlpatterns = [
    # Rutas personalizadas
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('employee-info/', employee_info, name='employee_info'),
    
    # Rutas para JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
