from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Teacher, Department
from subjects.models import Subject
from .forms import TeacherForm
from django.contrib.auth.mixins import LoginRequiredMixin

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    context_object_name = 'teachers'

    def get_queryset(self):
        queryset = Teacher.objects.all()
        query = self.request.GET.get('q', '').strip()
        department = self.request.GET.get('department', '').strip()
        subject = self.request.GET.get('subject', '').strip()
        status = self.request.GET.get('status', '').strip()

        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(email__icontains=query)
            )

        if department:
            queryset = queryset.filter(department_id=department)

        if subject:
            queryset = queryset.filter(subjects__id=subject)

        if status:
            queryset = queryset.filter(is_active=(status == 'active'))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'departments': Department.objects.all(),
            'subjects': Subject.objects.all(),
            'search_query': self.request.GET.get('q', ''),
            'department_filter': self.request.GET.get('department', ''),
            'subject_filter': self.request.GET.get('subject', ''),
            'status_filter': self.request.GET.get('status', ''),
        })
        return context

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'
    context_object_name = 'teacher'

    def get_object(self, queryset=None):
        return Teacher.objects.get(
            created_at__year=self.kwargs['year'],
            created_at__month=self.kwargs['month'],
            created_at__day=self.kwargs['day'],
            slug=self.kwargs['slug']
        )

class TeacherCreateView(LoginRequiredMixin,CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/form.html'
    success_url = reverse_lazy('teachers:list')

    def get_success_url(self):
        return self.object.get_detail_url()

class TeacherUpdateView(LoginRequiredMixin,UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/form.html'
    success_url = reverse_lazy('teachers:list')

    def get_success_url(self):
        return self.object.get_detail_url()

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teachers/confirm-delete.html'
    success_url = reverse_lazy('teachers:list')
