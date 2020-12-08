from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('hire-me/', views.hire_me, name='hire-me'),
    path('upload/', views.upload, name='upload'),
]
