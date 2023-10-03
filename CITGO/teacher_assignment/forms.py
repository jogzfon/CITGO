from django import forms
from .models import Teacher

class TeacherAssignmentForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['subjects_taught']
