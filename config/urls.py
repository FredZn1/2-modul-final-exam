from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from departments.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('departments/', include('departments.urls')),
    path('groups/', include('groups.urls')),
    path('students/', include('students.urls')),
    path('subjects/', include('subjects.urls')),
    path('teachers/', include('teachers.urls')),
    path('users/', include('users.urls')),
    path('', HomePageView.as_view(), name='home')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)