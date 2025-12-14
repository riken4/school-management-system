from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, Add_Student, Student, SchoolClassForm
from .models import CustomUser, School_Class, herosection
from django.contrib.auth.models import User





def home(request):
    context = {}

    return render(request, 'home.html')

def signup_view(request): 
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
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
    teachers = CustomUser.objects.filter(user_type='teacher')
    classes = School_Class.objects.filter()
    hero = herosection.objects.get(is_active=True)
    print("Current User:", user)

    return render(request, 'dashboard.html', {
        'user': user,
        'students': students,
        'teachers': teachers,
        'hero': hero,
        'classes': classes,
    })

def school_class(request, id):
    
    teacher = CustomUser.objects.get(id=id, user_type='teacher') 
    classes = School_Class.objects.get(teacher=teacher)
    students = classes.student.all()
    
    # students = CustomUser.objects.filter(classes__in=classes).distinct()
    return render(request, 'school_class.html', {
        'teacher': teacher,
        'classes': classes,
        'students': students,
    })

def add_student(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():     
            form.save()
            return redirect('student_list') 
    else: 
        form = CustomUserCreationForm()
    return render(request, 'add_student.html', {'form': form})

def student_list(request):
    students = CustomUser.objects.filter(user_type='student')
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, id):
    student = get_object_or_404(CustomUser, id=id, user_type='student')
    classes = student.classes.all()
    
    return render(request, 'student_detail.html', {
        'student': student,
        'classes': classes,
    })

def student_update(request, id):
    student = get_object_or_404(CustomUser, id=id)
    form = CustomUserCreationForm(request.POST or None, instance=student)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('student_list')

    return render(request, 'student_update.html', {'form': form})

def student_delete(request, id):
    student = get_object_or_404(CustomUser, id=id, user_type='student')
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'student_delete.html', {'student': student})


def add_teacher(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():     
            form.save()
            return redirect('dashboard') 
    else: 
        form = CustomUserCreationForm()
    return render(request, 'add_teacher.html', {'form': form})

def teacher_list(request):
    teachers = CustomUser.objects.filter(user_type='teacher')
    return render(request, 'teacher_list.html', {'teachers': teachers})

def teacher_detail(request, id):
    teacher = get_object_or_404(CustomUser, id=id, user_type='teacher')
    classes = School_Class.objects.filter(teacher=teacher)
    
    return render(request, 'teacher_detail.html', {
        'teacher': teacher,
        'classes': classes,
    })

def teacher_update(request, id):
    teacher = get_object_or_404(CustomUser, id=id)
    form = CustomUserCreationForm(request.POST or None, instance=teacher)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('teacher_list')

    return render(request, 'teacher_update.html', {'form': form})

def teacher_delete(request, id):
    teacher = get_object_or_404(CustomUser, id=id, user_type='teacher')
    if request.method == "POST":
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'teacher_delete.html', {'teacher': teacher})





def student_class_detail(request, id):
    student = CustomUser.objects.get(id=id, user_type='student')
    classes = student.classes.all()  
    return render(request, "student_class_detail.html", {
        "student": student,
        "classes": classes,
    })


def class_list(request):
    classes = School_Class.objects.all()
    return render(request, 'class_list.html', {'classes': classes})

def class_create(request):
    if request.method == 'POST':
        form = SchoolClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = SchoolClassForm()
    return render(request, 'class_create.html', {'form': form})

def class_update(request, id):
    school_class = get_object_or_404(School_Class, id=id)
    if request.method == 'POST':
        form = SchoolClassForm(request.POST, instance=school_class)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = SchoolClassForm(instance=school_class)
    return render(request, 'class_create.html', {'form': form})

def class_delete(request, id):
    school_class = get_object_or_404(School_Class, id=id)
    if request.method == 'POST':
        school_class.delete()
        return redirect('class_list')
    return render(request, 'class_delete.html', {'class': school_class})