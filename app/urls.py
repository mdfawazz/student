from django.urls import path
from . import views
urlpatterns = [
    path('',views.update),
    path('add',views.update),
    path('delete',views.delete),
    path('update',views.up),
    path('updation',views.delete),
    path('tables',views.tables),
    path('delete2',views.delete2),
]
