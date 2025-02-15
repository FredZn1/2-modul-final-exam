from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Subject, Department
from .forms import SubjectForm


class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects/list.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        queryset = Subject.objects.all()
        query = self.request.GET.get('q', '').strip()
        department = self.request.GET.get('department', '').strip()
        status = self.request.GET.get('status', '').strip()

        if query:
            queryset = queryset.filter(Q(name__icontains=query))

        if department:
            queryset = queryset.filter(department_id=department)

        if status:
            queryset = queryset.filter(status=(status == 'active'))

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'departments': Department.objects.all(),
            'search_query': self.request.GET.get('q', ''),
            'department_filter': self.request.GET.get('department', ''),
            'status_filter': self.request.GET.get('status', ''),
        })
        return context

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subjects/detail.html'
    context_object_name = 'subject'

    def get_object(self, queryset=None):
        return Subject.objects.get(slug=self.kwargs['slug'])


class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subjects/form.html'
    success_url = reverse_lazy('subjects:list')

    def get_success_url(self):
        return self.object.get_detail_url()


class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subjects/form.html'
    success_url = reverse_lazy('subjects:list')

    def get_success_url(self):
        return self.object.get_detail_url()


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'subjects/confirm-delete.html'
    success_url = reverse_lazy('subjects:list')
