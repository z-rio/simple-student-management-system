from . import views
from django.urls import path

urlpatterns = [
    path('students/', views.StudentListCreateView.as_view(), name='student-list-create'),
]