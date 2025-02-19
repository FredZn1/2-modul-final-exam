from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, UpdateView, View
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm
from .models import UserProfile


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response


class UserLoginView(FormView):
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
            return redirect(self.success_url)
        return self.form_invalid(form)


class UserLogoutView(View):

    def post(self, request):
        logout(request)
        return redirect('users:login')


class UpdateProfileView(LoginRequiredMixin, UpdateView):

    model = UserProfile
    form_class = UserProfileForm
    template_name = 'users/profile-update.html'
    success_url = reverse_lazy('users:profile_update')

    def get_object(self, queryset=None):
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return profile

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class SuccessLogoutView(View):

    def get(self, request):
        return render(request, 'users/logout.html')
