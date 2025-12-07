from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('school_class/<int:id>/', views.school_class, name='school_class'),
    path('add_student/', views.add_student, name='add_student'),
]