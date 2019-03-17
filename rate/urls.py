from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('profile/',views.profile,name='profile'),
   path('register/',views.register,name='register'),
   path('profile/update',views.edit_profile,name='update_profile'),
   path('project/new',views.new_project,name='new_project'),
   path('project/view/<int:id>',views.project_view,name='project_view')
]