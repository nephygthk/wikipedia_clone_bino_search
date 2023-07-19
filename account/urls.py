from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),
    path('add_new_profile/', views.add_new_profile, name='add_new_profile'),
    path('search/result/<slug>', views.search_result, name='search_result'),
    path('delete_profile/<slug>/', views.delete_profile, name='delete_profile'),
    path('edit_profile/<slug>/', views.edit_profile, name='edit_profile'),
]