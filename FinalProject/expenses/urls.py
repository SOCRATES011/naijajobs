from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('groups/<int:group_id>/', views.group_detail, name='group_detail'),
    path('groups/<int:group_id>/expenses/new/', views.create_expense, name='create_expense'),
]
