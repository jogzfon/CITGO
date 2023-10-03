from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Teacher
from .forms import TeacherAssignmentForm

def teacher_assignment(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)

    if request.method == 'POST':
        form = TeacherAssignmentForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')

    else:
        form = TeacherAssignmentForm(instance=teacher)

    return render(request, 'teacher_assignment/teacher_assignment_form.html', {'form': form})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_assignment/teacher_list.html', {'teachers': teachers})
