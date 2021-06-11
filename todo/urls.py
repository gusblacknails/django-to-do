from django.urls import path, include, re_path
from rest_framework import routers
from knox import views as knox_views

from .views import TaskListView, FluTodoLoginView, new_user, TaskDeleteView
from .api.views import LoginAPI, TaskCreateApi, TaskApi, CreateUserAPI
from django.contrib.auth.views import LogoutView

router = routers.DefaultRouter()

urlpatterns = [
    path('', TaskListView.as_view(), name='task'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
    path('login/', FluTodoLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', new_user, name='signup'),

    # API

    path('api/',TaskApi.as_view()),
    path('api/create/',TaskCreateApi.as_view(), name='create'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/register/', CreateUserAPI.as_view(), name='register'), 
]
