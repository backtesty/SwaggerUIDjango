from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView,\
     TokenRefreshView, TokenVerifyView, TokenBlacklistView
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from .views import DocsView, RedocView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('api_schema/v1/', get_schema_view(title='API Django Schema',\
        description='Servicios (APIs) de la aplicación tarea', version='1.0.0'), name='api_schema'),
    path('docs/', DocsView.as_view(), name='swagger-ui'),
    path('redoc/', RedocView.as_view(), name='redoc'),
    # JWT Token
    path('api-auth/token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api-auth/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    # Rest Framework Auth
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-v1/', include('app_tasks.urls', namespace='tasks')),
]
