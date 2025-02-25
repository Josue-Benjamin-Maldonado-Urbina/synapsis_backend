from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from .models import Owner, Pet
import json

@csrf_exempt
def add_owner(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            owner = Owner.objects.create(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                phone_number=data.get('phone_number'),
                address=data.get('address'),
            )
            return JsonResponse({'message': 'Owner added successfully', 'owner_id': owner.id}, status=201)
        except IntegrityError:
            return JsonResponse({'error': 'Este dueño ya existe. Por favor verifica el nombre y apellido.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def delete_owner(request, owner_id):
    if request.method == 'DELETE':
        try:
            owner = get_object_or_404(Owner, id=owner_id)
            owner.delete()
            return JsonResponse({'message': 'Dueño eliminado con éxito.'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Método no permitido.'}, status=405)

def get_owners(request):
    if request.method == 'GET':
        owners = Owner.objects.all().values('id', 'first_name', 'last_name')
        return JsonResponse(list(owners), safe=False)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def add_pet(request):
    if request.method == 'POST':
        try:
            # Recuperar datos del formulario
            data = request.POST
            image = request.FILES.get('image')  # Obtener la imagen desde los archivos subidos
            owner = get_object_or_404(Owner, id=data.get('owner'))
            
            # Crear la nueva mascota
            pet = Pet.objects.create(
                name=data.get('name'),
                category=data.get('category'),
                gender=data.get('gender'),
                birth_date=data.get('birth_date'),
                breed=data.get('breed'),
                description=data.get('description'),
                illness=data.get('illness'),
                illness_gravity=data.get('illness_gravity'),
                owner=owner,
                image=image,
            )
            return JsonResponse({'message': 'Mascota registrada con éxito', 'pet_id': pet.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def get_pets(request):
    if request.method == 'GET':
        pets = Pet.objects.select_related('owner').all()
        pets_data = [
            {
                'id': pet.id,
                'name': pet.name,
                'category': pet.get_category_display(),
                'image': request.build_absolute_uri(pet.image.url) if pet.image else None,  # URL completa
                'description': pet.description,
                'birth_date': pet.birth_date.strftime('%Y-%m-%d') if pet.birth_date else None,
                'owner': {
                    'first_name': pet.owner.first_name,
                    'last_name': pet.owner.last_name,
                    'phone_number': pet.owner.phone_number,
                    'address': pet.owner.address,
                },
            }
            for pet in pets
        ]
        return JsonResponse(pets_data, safe=False)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def delete_pet(request, id):
    """
    Eliminar una mascota por ID.
    """
    if request.method == 'DELETE':
        pet = get_object_or_404(Pet, id=id)
        pet.delete()
        return JsonResponse({'message': 'Mascota eliminada exitosamente'}, status=200)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def update_pet(request, id):
    """
    Actualizar los datos de una mascota por ID.
    """
    if request.method == 'PUT':
        pet = get_object_or_404(Pet, id=id)
        try:
            data = json.loads(request.body)  # Parsear el JSON enviado desde el frontend
            pet.name = data.get('name', pet.name)
            pet.category = data.get('category', pet.category)
            pet.description = data.get('description', pet.description)
            pet.gender = data.get('gender', pet.gender)
            pet.birth_date = data.get('birth_date', pet.birth_date)
            pet.save()
            return JsonResponse({'message': 'Mascota actualizada exitosamente'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos'}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)