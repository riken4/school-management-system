# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
# from django.contrib import messages
# from .forms import CustomUserCreationForm
# from .models import Teacher, Student, School_Class


# def home(request):
#     return render(request, 'home.html')


# def signup_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect('login')
#         else:
#             for field, errors in form.errors.items():
#                 for error in errors:
#                     messages.error(request, f'{field}: {error}')
#     else:
#         form = CustomUserCreationForm()
    
#     return render(request, 'signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             messages.success(request, f'Welcome back, {user.username}!')
#             if user.is_admin:
#                 return redirect('admin_dashboard')

#             elif user.is_teacher:
#                 return redirect('teacher_dashboard')

#             elif user.is_student:
#                 return redirect('student_dashboard')

#             elif user.is_staff_member:
#                 return redirect('staff_dashboard')

#         else:
#             messages.error(request, 'Invalid username or password!')
    
#     return render(request, 'login.html')

# def logout_view(request):
#     logout(request)
#     messages.success(request, 'You have been logged out successfully!')
#     return redirect('login') 

# def admin_dashboard(request):
#     return render(request, 'admin/admin_dashboard.html')

# def teacher_dashboard(request, teacher_id):
#     teachers = Teacher.objects.all() 
#     return render(request, 'teacher/teacher_dashboard.html', {'teachers': teachers})

# def teacher_detail(request):
#     return render(request, 'teacher/teacher_detail.html')

# def student_dashboard(request):
#     students = Student.objects.all()
#     return render(request, 'student/student_dashboard.html',{'students': students})

# def staff_dashboard(request):
#     return render(request, 'staff/staff_dashboard.html')

# def school_class(request):
#     school_class = School_Class.objects.all() 
#     return render(request, 'school_class.html', {'school_class': school_class})


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import CustomUser, School_Class



def home(request):
    context = {}
    # if request.user.is_authenticated:
    #     teachers = Teacher.objects.all()
    #     classes = School_Class.objects.all()
    #     students = Student.objects.all()
    #     context = {
    #         'teachers': teachers,
    #         'classes': classes,
    #         'students': students
    #     }
    return render(request, 'home.html')

def signup_view(request): 
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')

            if user.is_admin:
                return redirect('dashboard')

            elif user.is_teacher:
                return redirect('dashboard')

            elif user.is_student:
                return redirect('dashboard')

            elif user.is_staff_member:
                return redirect('dashboard')

        else:
            messages.error(request, 'Invalid username or password!')
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('login') 

def dashboard(request):
    user = request.user

    students = CustomUser.objects.filter(user_type='student')

    print("Current User:", user)

    return render(request, 'dashboard.html', {
        'user': user,
        'students': students,
    })


def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')



def teacher_detail(request):
    return render(request, 'teacher/teacher_detail.html')



def staff_dashboard(request):
    return render(request, 'staff/staff_dashboard.html')


def school_class(request):
    school_class = School_Class.objects.all() 
    return render(request, 'school_class.html', {'school_classes': school_class})
