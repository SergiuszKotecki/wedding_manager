from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt import views as jwt_views

from adverts.urls import router as adverts_router
from guests.urls import router as guest_router
from patches import routers
from users.urls import router as users_router

router = routers.DefaultRouter()
router.extend(users_router)
router.extend(adverts_router)
router.extend(guest_router)

schema_view = get_schema_view(
    openapi.Info(
        title="Wedding planner API",
        default_version='v3',
        description="Wedding planner SWAGGER",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sergiusz.kotecki@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

v = settings.API_VERSION

urlpatterns = [
    # Admin page
    re_path(r'^jet/', include('jet.urls', 'jet')),
    re_path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    # re_path(r'^api-auth/', include('rest_framework.urls')),
    # Router endpoints
    path(f'{v}/', include(router.urls)),
    # JWToken endpoints
    path(f'{v}/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{v}/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # Documentation endpoints
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
