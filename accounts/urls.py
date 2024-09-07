from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', views.home, name='home'),  # API home endpoint
    path('animals/', views.animal_management, name='animal_management'),  # Animal management (GET, POST, PUT, DELETE)
    path('login/', views.viewlog, name='login'),  # User login
    path('signup/', views.viewsign, name='signup'),  # User signup
    path('api/animals/', views.AnimalListCreateView.as_view(), name='animal_list_create'),  # DRF generic animal list/create
    path('api/animals/<int:pk>/', views.AnimalDetailView.as_view(), name='animal_detail'),  # DRF generic animal detail (retrieve, update, delete)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Add support for format suffixes (e.g., .json)
urlpatterns = format_suffix_patterns(urlpatterns)
