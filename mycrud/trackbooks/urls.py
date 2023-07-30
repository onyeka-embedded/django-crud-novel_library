from django.urls import path
from . import views

urlpatterns = [
    path('', views.allNovels, name='allnovels'),
    path('novel/<str:pk>/', views.getNovel, name='novel'),
    path('add-novel/', views.addNovel, name='add_novel'),
    path('update-novel/<str:pk>/', views.updateProject, name='update_novel'),
    path('delete-novel/<str:pk>/', views.deleteNovel, name="delete-novel"),
]