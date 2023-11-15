from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='index'),
    path('form/<int:pk>', views.FormDetailView.as_view(), name='form_detail'),
    path('form/entry/<int:pk>', views.FormEntryDetailView.as_view(), name='form_entry'),
    path('login', auth_views.LoginView.as_view(template_name='simple_msg_server/login.html'), name='login'),
    # path('logout', auth_views.LogoutView.as_view(), name='logout'),
]
