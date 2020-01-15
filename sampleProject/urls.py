"""sampleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from sample_app import views
from rest_framework.authtoken import views as authViews

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Sample API",
      default_version='v1',
      description="Sample",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'post', views.postViewSet)

# Admin Customization
admin.site.site_header = "Sample Project"
admin.site.site_title = "Sample Project: Admin Panel"
admin.site.index_title = "Sample Project"

# URL's
urlpatterns = [
  	path(r'', include('sample_app.urls')),
  	path(r'api/', include(router.urls)),
    path(r'admin/', admin.site.urls),
    path(r'o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
