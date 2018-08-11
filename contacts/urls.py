from django.urls import include, path
from . import views

urlpatterns = [
    # TODO: this path is not working
    path('', views.index, name='index'),
]