from django.urls import path
from .views import (
    AboutUsListCreateView,
    AboutUsRetrieveUpdateDestroyView,
    PersonListCreateView,
    PersonRetrieveUpdateDestroyView,
    OrganizationUnitListCreateView,
    OrganizationUnitRetrieveUpdateDestroyView,
)

urlpatterns = [
    # AboutUs endpoints
    path('', AboutUsListCreateView.as_view(), name='about_us'),
    path('<int:pk>/', AboutUsRetrieveUpdateDestroyView.as_view(), name='about_us_detail'),

    # People endpoints
    path('people/', PersonListCreateView.as_view(), name='people'),
    path('people/<int:pk>/', PersonRetrieveUpdateDestroyView.as_view(), name='person_detail'),

    # OrganizationUnit endpoints
    path('units/', OrganizationUnitListCreateView.as_view(), name='organization_units'),
    path('units/<int:pk>/', OrganizationUnitRetrieveUpdateDestroyView.as_view(), name='organization_unit_detail'),
]
