from django import forms
from .models import FeedBack

class TeacherAssignmentForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['subjects_taught']
