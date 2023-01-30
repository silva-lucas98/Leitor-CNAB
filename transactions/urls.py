from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name="file_txt"),
    path('list/', views.list_data_stores)
]