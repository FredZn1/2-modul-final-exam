from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Group
from .forms import GroupForm


class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'
    context_object_name = 'groups'
    paginate_by = 10  # Sahifadagi obyektlar soni

    def get_queryset(self):
        queryset = Group.objects.all()
        query = self.request.GET.get('q')
        filter_date = self.request.GET.get('date')

        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))

        if filter_date:
            queryset = queryset.filter(created_at__date=filter_date)

        return queryset


class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/detail.html'
    context_object_name = 'group'

    def get_object(self, queryset=None):
        return Group.objects.get(
            created_at__year=self.kwargs['year'],
            created_at__month=self.kwargs['month'],
            created_at__day=self.kwargs['day'],
            slug=self.kwargs['slug']
        )


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/form.html'
    success_url = reverse_lazy('groups:list')

    def get_success_url(self):
        return self.object.get_detail_url()


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/form.html'
    success_url = reverse_lazy('groups:list')

    def get_success_url(self):
        return self.object.get_detail_url()


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'groups/confirm-delete.html'
    success_url = reverse_lazy('groups:list')
