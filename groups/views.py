from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Group, Teacher
from .forms import GroupForm
from django.contrib.auth.mixins import LoginRequiredMixin


class GroupListView(ListView):
    model = Group
    template_name = "groups/list.html"
    context_object_name = "groups"


    def get_queryset(self):
        queryset = Group.objects.all()


        grade_level = self.request.GET.get("grade_level")
        teacher = self.request.GET.get("teacher")
        status = self.request.GET.get("status")
        query = self.request.GET.get("q")

        if grade_level:
            queryset = queryset.filter(grade_level=grade_level)
        if teacher:
            queryset = queryset.filter(teacher_id=teacher)
        if status == "active":
            queryset = queryset.filter(status=True)
        elif status == "inactive":
            queryset = queryset.filter(status=False)
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teachers"] = Teacher.objects.all()
        return context



class GroupDetailView(DetailView):
    model = Group
    template_name = "groups/detail.html"
    context_object_name = "group"

    def get_object(self, queryset=None):
        return get_object_or_404(
            Group,
            created_at__year=self.kwargs['year'],
            created_at__month=self.kwargs['month'],
            created_at__day=self.kwargs['day'],
            slug=self.kwargs['slug']
        )



class GroupCreateView(LoginRequiredMixin,CreateView):
    model = Group
    form_class = GroupForm
    template_name = "groups/form.html"
    success_url = reverse_lazy("groups:list")

    def get_success_url(self):
        return self.object.get_detail_url()



class GroupUpdateView(LoginRequiredMixin,UpdateView):
    model = Group
    form_class = GroupForm
    template_name = "groups/form.html"
    success_url = reverse_lazy("groups:list")

    def get_success_url(self):
        return self.object.get_detail_url()



class GroupDeleteView(DeleteView):
    model = Group
    template_name = "groups/confirm-delete.html"
    success_url = reverse_lazy("groups:list")



class TeacherListView(ListView):
    model = Teacher
    template_name = "teachers/list.html"
    context_object_name = "teachers"
