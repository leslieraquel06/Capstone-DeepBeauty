"""
URL configuration for deepbeauty project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from skincare import views
from skincare.views import ItemSearchAPIView, ItemViewSet, MoistViewSet, PostViewSet, SunViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('itemdata',ItemViewSet, basename='itemdata')
router.register('moisturizer', MoistViewSet, basename='moisturizer')
router.register('sunblock', SunViewSet, basename='sunblock')
router.register('allpost', PostViewSet, basename='allpost')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('skincare.urls')),
    path('',include(router.urls)),
    path('api/search/', ItemSearchAPIView.as_view(), name='item-search'),
    path('community/', views.community,name='community'),
    path('home/', views.home,name='home'),
    path('product/', views.home,name='product'),
    path('quiz/', views.quiz, name='quiz'),
    path('createpost/', views.createpost, name='createpost')
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
