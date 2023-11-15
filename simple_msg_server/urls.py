from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='index'),
    path('form/<int:pk>', views.FormDetailView.as_view(), name='form_detail')
    # path('login', auth_views.LoginView.as_view(), name='login'),
    # path('logout', auth_views.LogoutView.as_view(), name='logout'),
]
