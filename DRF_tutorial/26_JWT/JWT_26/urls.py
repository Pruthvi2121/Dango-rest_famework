"""JWT_26 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

router = DefaultRouter()
router.register('StudentAPI/', views.StudentModelViewSet, basename='StudentAPI')

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('gettoken/', TokenObtainPairView.as_view()  , name='gettoken'),
    path('verify/', TokenVerifyView.as_view(), name='tokenverify'),
    path('refresh/', TokenRefreshView.as_view(), name='tokenrefresh'),

]
