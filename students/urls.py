from django.urls import path
from .views import StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView

app_name = 'students'

urlpatterns = [
    path('list/', StudentListView.as_view(), name='list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', StudentDetailView.as_view(), name='detail'),
    path('create/', StudentCreateView.as_view(), name='create'),
    path('<int:pk>/update/', StudentUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='delete'),
]
