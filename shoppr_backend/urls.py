from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import test
from .views import user
from .views import auth

urlpatterns = [
    path('test_app_endpoint/', test.TestView.as_view(), name='app_test'),
    path('test/', auth.AccessTokenView.as_view(), name='test'),
    path('register/', user.Register.as_view(), name='register_user'),
    path('login/', user.Login.as_view(), name='login'),
    # path('users/', user.UserView.as_view(), name='users'),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

