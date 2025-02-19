# from django.contrib.auth import login, authenticate
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView, UpdateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response

class UserLoginView(FormView):
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        return self.form_invalid(form)

class ProfileView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user.profile

# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('accounts:profile')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': form})
#
# def user_login(request):
#     if request.method == 'POST':
#         form = CustomAuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('accounts:profile')
#     else:
#         form = CustomAuthenticationForm()
#     return render(request, 'accounts/login.html', {'form': form})
#
# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             return redirect('accounts:profile')
#     else:
#         form = UserProfileForm(instance=request.user.profile)
#     return render(request, 'accounts/profile.html', {'form': form})
#
