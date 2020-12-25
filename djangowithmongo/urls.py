from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

router = routers.SimpleRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Django with Mongo Integration - API Docs",
        default_version='v1',
        description="Django with MongoDB Integration API DOC",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="bugraahmetcaglar@gmail.com"),
        license=openapi.License(name="GNU License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        url(r'^', include(router.urls)),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        path("", include("user.urls")),
    ]
