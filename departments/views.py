from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Department



class HomePageView(TemplateView):
    template_name = 'dashboard.html'



class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/list.html'
    context_object_name = 'departments'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departments/detail.html'
    context_object_name = 'department'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'



class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'departments/form.html'
    fields = ['department_name', 'head_of_department', 'status', 'description', 'location', 'contact_email', 'contact_phone']
    success_url = reverse_lazy('departments:list')



class DepartmentUpdateView(UpdateView):
    model = Department
    template_name = 'departments/form.html'
    fields = ['department_name', 'head_of_department', 'status', 'description', 'location', 'contact_email', 'contact_phone']
    success_url = reverse_lazy('departments:list')



class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'departments/confirm_delete.html'
    success_url = reverse_lazy('departments:list')
