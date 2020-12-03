from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('/project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('/hire-me/', views.hire_me, name='hire-me'),
    path('/upload-image/', views.upload_image, name='upload-image'),
]
