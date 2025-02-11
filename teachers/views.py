from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Teacher
from .forms import TeacherForm


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    context_object_name = 'teachers'
    ordering = ['first_name', 'last_name']
    extra_context = {'title': 'Teachers List'}


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'
    context_object_name = 'teacher'
    extra_context = {'title': 'Teacher Detail'}


class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/form.html'

    def get_success_url(self):
        messages.success(self.request, "Teacher successfully created.")
        return reverse_lazy('teachers:list')


class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/form.html'

    def get_success_url(self):
        messages.success(self.request, "Teacher successfully updated.")
        return reverse_lazy('teachers:list')


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teachers/confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Teacher successfully deleted.")
        return reverse_lazy('teachers:list')

    def form_valid(self, form):
        messages.success(self.request, "Teacher deleted successfully.")
        return super().form_valid(form)
