from django.urls import path
from . import views
from .views import project_list, show_project_details, update_project, project_create, project_delete

app_name = 'projects'

urlpatterns = [
    path('', project_list.as_view(), name="list"),
    path('create/', project_create.as_view(), name="create"),
    path('<int:pk>/details', show_project_details.as_view(), name="detail"),
    path('<int:pk>/edit',update_project.as_view(), name="edit"),
    path('<int:pk>/delete',project_delete.as_view(), name="proddelete"),
]
