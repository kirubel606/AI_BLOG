from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUsListCreateView.as_view(), name='contact_us_list_create'),
    path('contact/<int:pk>/', views.ContactUsUpdateDeleteView.as_view(), name='contact_us_detail'),
    path('subscribe/', views.EmailSubscriptionView.as_view(), name='email_subscribe'),
]