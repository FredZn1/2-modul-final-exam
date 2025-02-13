from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import Department
from .forms import DepartmentForm

class HomePageView(ListView):
    model = Department
    template_name = 'dashboard.html'
    context_object_name = 'departments'
    paginate_by = 10

class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/list.html'
    context_object_name = 'departments'
    paginate_by = 10

    def get_queryset(self):
        queryset = Department.objects.all()
        head = self.request.GET.get('head_of_department', '').strip()
        status = self.request.GET.get('status', '').strip()

        if head:
            queryset = queryset.filter(head_of_department=head)

        if status:
            queryset = queryset.filter(status=status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['head_choices'] = getattr(Department, 'HEAD_CHOICES', [])
        context['status_choices'] = getattr(Department, 'STATUS_CHOICES', [])
        return context

class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departments/detail.html'
    context_object_name = 'department'

    def get_object(self, queryset=None):
        return get_object_or_404(
            Department,
            created_at__year=self.kwargs['year'],
            created_at__month=self.kwargs['month'],
            created_at__day=self.kwargs['day'],
            slug=self.kwargs['slug']
        )

class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'

    def get_success_url(self):
        return reverse(
            'departments:detail',
            kwargs={
                'year': self.object.created_at.year,
                'month': self.object.created_at.month,
                'day': self.object.created_at.day,
                'slug': self.object.slug
            }
        )

class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'

    def get_success_url(self):
        return reverse(
            'departments:detail',
            kwargs={
                'year': self.object.created_at.year,
                'month': self.object.created_at.month,
                'day': self.object.created_at.day,
                'slug': self.object.slug
            }
        )

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'departments/confirm-delete.html'
    success_url = reverse_lazy('departments:list')
