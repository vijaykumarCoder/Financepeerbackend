from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    # path('user/', views.get_user),
    path('login', views.login,name="login"),
    path('register', views.register,name="register"),
    path('upload', views.UploadJSON),
    path('allusers', views.AllUsers),
    path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    # path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall')
]