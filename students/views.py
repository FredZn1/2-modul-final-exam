from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student, Group
from .forms import StudentForm
from django.contrib.auth.mixins import LoginRequiredMixin

class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'

    def get_queryset(self):
        queryset = Student.objects.all()
        query = self.request.GET.get('q', '').strip()
        group = self.request.GET.get('group', '').strip()
        grade = self.request.GET.get('grade', '').strip()
        status = self.request.GET.get('status', '').strip()

        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(email__icontains=query)
            )

        if group:
            queryset = queryset.filter(group_id=group)

        if grade:
            queryset = queryset.filter(grade=grade)

        if status:
            queryset = queryset.filter(status=status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'groups': Group.objects.all(),
            'grade_choices': Student.GRADE_LEVEL_CHOICES,
            'status_choices': Student.STATUS_CHOICES,
            'search_query': self.request.GET.get('q', ''),
            'group_filter': self.request.GET.get('group', ''),
            'grade_filter': self.request.GET.get('grade', ''),
            'status_filter': self.request.GET.get('status', ''),
        })
        return context

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'
    context_object_name = 'student'

class StudentCreateView(LoginRequiredMixin,CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/form.html'
    success_url = reverse_lazy('students:list')

class StudentUpdateView(LoginRequiredMixin,UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/form.html'
    success_url = reverse_lazy('students:list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/confirm-delete.html'
    success_url = reverse_lazy('students:list')
