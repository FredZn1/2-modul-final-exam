from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import Department
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DepartmentForm


class HomePageView(LoginRequiredMixin, ListView):
    model = Department
    template_name = 'dashboard.html'
    context_object_name = 'departments'


class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/list.html'
    context_object_name = 'departments'


    def get_queryset(self):
        queryset = Department.objects.all()
        head = self.request.GET.get('head_of_department', '').strip()
        status = self.request.GET.get('status', '').strip()

        if head:
            queryset = queryset.filter(head_of_department__icontains=head)

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
            created_at__year=self.kwargs.get('year'),
            created_at__month=self.kwargs.get('month'),
            created_at__day=self.kwargs.get('day'),
            slug=self.kwargs.get('slug')
        )


class DepartmentCreateView(LoginRequiredMixin,CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'

    def get_success_url(self):
        if hasattr(self.object, 'created_at') and hasattr(self.object, 'slug'):
            return reverse(
                'departments:detail',
                kwargs={
                    'year': self.object.created_at.year,
                    'month': self.object.created_at.month,
                    'day': self.object.created_at.day,
                    'slug': self.object.slug
                }
            )
        return reverse_lazy('departments:list')


class DepartmentUpdateView(LoginRequiredMixin,UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'

    def get_success_url(self):
        if hasattr(self.object, 'created_at') and hasattr(self.object, 'slug'):
            return reverse(
                'departments:detail',
                kwargs={
                    'year': self.object.created_at.year,
                    'month': self.object.created_at.month,
                    'day': self.object.created_at.day,
                    'slug': self.object.slug
                }
            )
        return reverse_lazy('departments:list')


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'departments/confirm-delete.html'
    success_url = reverse_lazy('departments:list')