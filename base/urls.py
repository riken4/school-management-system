from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('teacher_detail/', views.teacher_detail, name='teacher_detail'),
    path('school_class/', views.school_class, name='school_class'),

]