from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, worker, Student

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(
        choices=CustomUser.USER_TYPE_CHOICES,
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type', 'password1', 'password2','name','address')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.user_type = self.cleaned_data['user_type']
        if commit:
            user.save()
        return user

class workerform(forms.ModelChoiceField):
    class meta:
        model=worker
        fields= '__all__'
from django import forms
from .models import Student

class Add_Student(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'student_class', 'section', 'image']
