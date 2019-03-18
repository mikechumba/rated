from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
   path('', views.home, name='home'),
   path('profile/',views.profile,name='profile'),
   path('register/',views.register,name='register'),
   path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm,extra_context={'title': 'Login'}), name='login'),
   path('logout/', views.logout_view, name='logout'),
   path('profile/update',views.edit_profile,name='update_profile'),
   path('project/new',views.new_project,name='new_project'),
   path('project/view/<int:id>',views.project_view,name='project_view'),
   path('search/',views.search,name="search"),
   # Extra views
   path('api/profiles/',views.ProfileList.as_view())
]