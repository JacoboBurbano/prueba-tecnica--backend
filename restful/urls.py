"""
URL configuration for restful project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from views.views import home

schema_view = get_schema_view(
    openapi.Info(
        title="API de Usuarios",
        default_version="v1",
        description="User Management API Documentation with Django and JWT",
        license=openapi.License(name="Licencia MIT"),
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path('views/', include('views.urls'))
]
