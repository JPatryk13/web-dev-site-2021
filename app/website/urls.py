from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('contact-success/', views.contact_success, name='contact-success'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('hire-me/', views.HireMe.as_view(), name='hire-me'),
    path('hire-me-success/', views.hire_me_success, name='hire-me-success'),
    path('upload/', views.upload, name='upload'),
]
