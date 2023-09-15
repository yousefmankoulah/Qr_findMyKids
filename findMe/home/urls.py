from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/<id>/', views.dashboard, name="dashboard"),
    path('login/', views.signInView, name='login'),
    path('logout/', views.signoutView, name='logout'),
    path('register/', views.register, name="register"),
    path('createQR/', views.createQR, name="createQR"),
    path('profileDetail/<id>/', views.profileDetail, name="profileDetail"),
    path('updateProfile/<int:id>/', views.updateProfile, name="updateProfile"),
    path('delete/<int:id>/', views.delete_post, name="delete"),


#     path("set_language/<str:user_language>/", views.set_language_from_url, name="set_language_from_url"),



    #password reset
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'),
         name='password_reset_complete'),

    #end password reset

    
]