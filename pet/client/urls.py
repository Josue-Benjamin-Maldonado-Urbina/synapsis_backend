from django.urls import path
from .views import add_owner, add_pet, delete_owner, get_owners, get_pets, delete_pet, update_pet

urlpatterns = [
    path('add-owner/', add_owner, name='add_owner'),
    path('delete-owner/<int:owner_id>/', delete_owner, name='delete_owner'),
    path('owners/', get_owners, name='get_owners'),
    path('add-pet/', add_pet, name='add_pet'),
    path('pets/', get_pets, name='get_pets'),
    path('delete-pet/<int:id>/', delete_pet, name='delete_pet'),
    path('update-pet/<int:id>/', update_pet, name='update_pet'),
]