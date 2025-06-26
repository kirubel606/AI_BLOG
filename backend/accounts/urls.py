from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .serializers import MyTokenObtainPairView
from accounts.views import SignupView, UserDetailView, UsersListView,PermissionsListView

urlpatterns = [
    path('all/', UsersListView.as_view(), name='all_users'),
    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('user/delete/<uuid:pk>/', UserDetailView.as_view(), name='user_delete'),
    path('user/signup/', SignupView.as_view(), name='user_signup'),
    path('user/update/<uuid:pk>/', SignupView.as_view(), name='user_update'),
    path('user/login/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('permissions/', PermissionsListView.as_view(), name='permissions_list'),

]