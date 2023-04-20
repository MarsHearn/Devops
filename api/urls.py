from django.urls import path, include
from . import views
from rest_framework import routers
from django.urls import re_path

#from rest_framework.authtoken import views as view2
'''from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)'''
router = routers.DefaultRouter()
router.register(r'test1', views.test_viewset)
urlpatterns = [
    path('', include(router.urls)),
    #path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('api-auth/', include('rest_auth.urls')),
    #path('api-token-auth/', include(view2.obtain_auth_token)),
    #path('account/', include('allauth.urls')), # user sign up
    #path('rest-auth/', include('rest_auth.urls')),
    #re_path(r'^rest-auth/', include('rest_auth.urls'))
    path('api-auth/', include('rest_framework.urls')),
    
    
]