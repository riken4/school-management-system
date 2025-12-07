from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, Add_Student
from .models import CustomUser, School_Class, herosection
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



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
            print('yes')
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
    teachers = CustomUser.objects.filter(user_type='teacher')
    hero = herosection.objects.get(is_active=True)
    print("Current User:", user)

    return render(request, 'dashboard.html', {
        'user': user,
        'students': students,
        'teachers': teachers,
        'hero': hero,
    })



def school_class(request, teacher_id):
    user = get_object_or_404(user, id=teacher_id)
    return render(request, 'school_class.html', {'user': user})
# def school_class(request):
    # T=School_Class.objects.get(class_name='class 2')
    # print(T)
    # school_classes = School_Class.objects.get(teacher__id=id)
    # school_classes = School_Class.objects.filter(teacher__id=id)
    # section = School_Class.objects.filter(teacher__id=id)
    teacher = CustomUser.objects.get(id=id)
    classes = School_Class.objects.filter(teacher=teacher)
    return render(request, 'school_class.html', {
        'teacher': teacher,
        'classes': classes
    })
    
    # school_classes = School_Class.objects.get(id=id)
    return render(request, school_class.html)
        # 'school_classes': school_classes,

        # 'school_classes': teacher})

def add_student(request):
    if request.method == 'POST':
        form = Add_Student(request.POST, request.FILES)

        if form.is_valid():
            print('yes')
            form.save()
            return redirect('dashboard') 
    else:
        form = Add_Student()
    return render(request, 'add_student.html', {'form': form})