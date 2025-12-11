from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, worker, Student, School_Class

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(
        choices=CustomUser.USER_TYPE_CHOICES,
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type', 'password1', 'password2','name','address','image')

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

class SchoolClassForm(forms.ModelForm):
    class Meta:
        model = School_Class
        fields = ['class_name', 'section', 'teacher', 'student']
        widgets = {
            'student': forms.CheckboxSelectMultiple,  
        }

        
class Add_Student(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'roll_number', 'address', 'image']

class Stu_class(forms.ModelForm):
    class Meta:
        model = School_Class
        fields = ['class_name', 'section', 'teacher']