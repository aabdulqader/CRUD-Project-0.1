from django.urls import path
from .views import (
    home,
    update,
    delete,
)

urlpatterns = [
    path('', home, name= 'home'),
    path('edit/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),  
]
