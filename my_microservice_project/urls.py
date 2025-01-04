"""
URL configuration for my_microservice_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
]

if 'users' in settings.ENABLED_APPS:
    urlpatterns.append(path('api/', include('users.urls')))
if 'products' in settings.ENABLED_APPS:
    urlpatterns.append(path('api/', include('products.urls')))


# Conditionally add app URLs based on environment variables
# if env('ENABLE_PRODUCT_APP', default='False') == 'True':
#     urlpatterns.append(path('api/', include('products.urls')))

# if env('ENABLE_USERS_APP', default='False') == 'True':
#     urlpatterns.append(path('api/', include('users.urls')))

# if env('ENABLE_heelo_APP', default='False') == 'True':
#     urlpatterns.append(path('api/', include('my_microservice_app.urls')))