from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('school_class/<int:id>', views.school_class, name='school_class'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),
    path('student_detail/<int:id>/', views.student_detail, name='student_detail'),
    path('student_update/<int:id>/', views.student_update, name='student_update'),
    path('student_delete/<int:id>/', views.student_delete, name='student_delete'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('teacher_list/', views.teacher_list, name='teacher_list'), 
    path('teacher_detail/<int:id>', views.teacher_detail, name='teacher_detail'), 
    path('teacher_update/<int:id>/', views.teacher_update, name='teacher_update'),
    path('teacher_delete/<int:id>/', views.teacher_delete, name='teacher_delete'),

    path("student/<int:student_id>/class/", views.student_class_detail, name="student_class_detail"),
    path('class_list/', views.class_list, name='class_list'),
    path('class_create', views.class_create, name='class_create'),
    path('class<int:id>/update/', views.class_update, name='class_update'),
    path('class/<int:id>/delete/', views.class_delete, name='class_delete'),
]