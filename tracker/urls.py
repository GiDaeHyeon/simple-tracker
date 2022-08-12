from django.urls import path

from . import views


urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('file-upload/', views.FileUploadView.as_view(), name='file_upload'),
    path('init/', views.DBInitializeView.as_view(), name='init')
]
