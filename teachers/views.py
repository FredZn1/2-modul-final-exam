from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Teacher
from .forms import TeacherForm

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    context_object_name = 'teachers'

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

class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/form.html'
    success_url = reverse_lazy('teachers:list')

    def get_success_url(self):
        return self.object.get_detail_url()


class TeacherUpdateView(UpdateView):
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
