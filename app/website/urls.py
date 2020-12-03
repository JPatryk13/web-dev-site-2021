from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('hire-me/', views.hire_me, name='hire-me'),
    path('image-upload/', views.image_upload, name='image-upload'),
]
