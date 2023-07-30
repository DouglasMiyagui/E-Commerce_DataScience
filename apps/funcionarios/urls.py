from django.urls import path
from funcionarios.views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
]