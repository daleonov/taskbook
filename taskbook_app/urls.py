from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('contents', views.contents),
    path('all', views.all_on_one_page),
    path('random', views.random),
    path('<str:title_machine_friendly>', views.single_task),
]
