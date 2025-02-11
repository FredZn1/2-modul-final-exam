from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Group
from .forms import GroupForm


class GroupListView(ListView):
    model = Group
    template_name = 'groups/group_list.html'
    context_object_name = 'groups'


class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/group_detail.html'
    context_object_name = 'group'


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/group_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/group_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'groups/group_confirm_delete.html'
    success_url = reverse_lazy('groups:list')
