from django.contrib import admin
from django.urls import path
from hood import views

urlpatterns=[
    path("", views.index, name="index"),
    path('create_profile',views.create_profile, name='create_profile'),
    path('profile/',views.profile,name = 'profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('create_hood',views.create_hood, name= 'create_hood'),
    path('hood/', views.hoods, name = 'hood'),
    path('join_hood/<name>', views.join_hood, name='join-hood'),
    path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
  
]

