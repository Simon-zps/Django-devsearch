from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    path('projects/', views.getProjects),
    path('projects/<str:pk>/', views.getProject),
    path('projects/<str:pk>/vote/', views.projectVote),

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #token stored in the browser usual lifetime 5mins
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]