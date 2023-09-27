from django.urls import path
from .views import index
from .views import delete, create, single_prof, update_prof

urlpatterns = [
    path('', index, name='index'),
    path(' delete/<int:id>/', delete, name='delete'),
    path('create/', create, name='create'),
    path('single_prof/<int:id>/', single_prof, name='single_prof'),
    path('update_prof/<int:id>/', update_prof, name='update_prof'),
]
