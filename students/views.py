from django.urls import  reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student
from .forms import StudentForm


class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'
    paginate_by = 10

    def get_queryset(self):
        queryset = Student.objects.all()
        query = self.request.GET.get('q', '').strip()
        group = self.request.GET.get('group', '').strip()

        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(email__icontains=query)
            )

        if group:
            queryset = queryset.filter(group__name__icontains=group)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'search_query': self.request.GET.get('q', ''),
            'group_filter': self.request.GET.get('group', ''),
        })
        return context


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'
    context_object_name = 'student'


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/form.html'

    def get_success_url(self):
        return reverse_lazy('students:detail', args=[self.object.pk])


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/form.html'

    def get_success_url(self):
        return reverse_lazy('students:detail', args=[self.object.pk])


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/confirm-delete.html'
    success_url = reverse_lazy('students:list')
