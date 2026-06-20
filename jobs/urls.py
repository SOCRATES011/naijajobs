from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),
    path('post/', views.post_job, name='post_job'),
    path('my-listings/', views.my_listings, name='my_listings'),
    path('about/', views.about, name='about'),
    # auth
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
