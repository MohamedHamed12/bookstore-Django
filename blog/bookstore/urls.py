"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
# from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as authviews
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('home/',home),
    # path('about/',about),
    # path('contact/',contactme),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    # path('contact/',views.contactme),
    path('profile/<str:pk>',views.profile,name='profile'),
    path('customer/',views.customer,name='customer'),
    path('create/',views.create,name='create'),
    path('createid/<str:pk>',views.createid ,name='createid'),
    path('update/<str:pk>',views.update,name='update'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('register',views.register,name='register'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('logout',views.userlogout,name='logout'),
    path('userprofile',views.userpofile,name='userprofile'),
    path('profile_info',views.profile_info,name='profile_info'),

    # path('reset_password' ,authviews.PasswordResetView.as_view() , name="reset_password"),
    # path('reset_password_sent' ,authviews.PasswordResetDoneView.as_view() , name="password_reset_done"),
    # path('reset/<uidb64>/<token>/' ,authviews.PasswordResetConfirmView.as_view() , name="password_reset_confirm"),
    # path('reset_password_complete' ,authviews.PasswordResetCompleteView.as_view() , name="password_reset_complete"),

# ]

    path('reset_password/',authviews.PasswordResetView.as_view(template_name="main/password_reset.html"),name='reset_password'),
    path('reset_password_sent/',authviews.PasswordResetDoneView.as_view(template_name="main/password_reset_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',authviews.PasswordResetConfirmView.as_view(template_name="main/password_reset_form.html"),name='password_reset_confirm'),
    path('reset_password_complete/',authviews.PasswordResetCompleteView.as_view(template_name="main/password_reset_done.html"),name='password_reset_complete'),
    


]